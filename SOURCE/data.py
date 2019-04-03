
import numpy as np
import cv2
import os
import config as config
import filterToGrav as filterGrav

class DATA():

    def __init__(self, dirname):
        """
        :param dirname:
        self.dir_path = os.path.join(config.DATA_DIR, dirname)

        #FOR TESTING
        self.filelist = os.listdir(self.dir_path)


        #FOR TRAINING
        self.filelist = []
        for folder in o s.listdir(self.dir_path):
            for file in os.listdir(self.dir_path + "/" + folder):
                self.filelist.append(self.dir_path + "/" + folder + "/" + file)



        self.batch_size = config.BATCH_SIZE
        self.size = len(self.filelist)
        self.data_index = 0
        """

        self.dir_path = dirname
        self.filelist = os.listdir(dirname)[0:80000:40]
        #self.filelist = os.listdir(dirname) #test için
        self.batch_size = config.BATCH_SIZE
        self.size = len(self.filelist)
        self.data_index = 0

    def read_img(self, filename):
        print(filename)
        img = cv2.imread(filename, 3)
        labimg = cv2.cvtColor(cv2.resize(img, (config.IMAGE_SIZE, config.IMAGE_SIZE)), cv2.COLOR_BGR2Lab)
        return np.reshape(labimg[:,:,0], (config.IMAGE_SIZE, config.IMAGE_SIZE, 1)), labimg[:, :, 1:]

    def read_img_grav(self, filename):
        #print(filename)
        greyimg, colorimg = filterGrav.gravurLike(filename)
        labimg_gry = cv2.cvtColor(cv2.resize(greyimg, (config.IMAGE_SIZE, config.IMAGE_SIZE)), cv2.COLOR_BGR2Lab)
        labimg_clr = cv2.cvtColor(cv2.resize(colorimg, (config.IMAGE_SIZE, config.IMAGE_SIZE)), cv2.COLOR_BGR2Lab)
        return np.reshape(labimg_gry[:, :, 0], (config.IMAGE_SIZE, config.IMAGE_SIZE, 1)), labimg_clr[:, :, 1:]


    def generate_batch(self):
        batch = []
        labels = []
        filelist = []
        for i in range(self.batch_size):
            filename = os.path.join(config.DATA_DIR, self.dir_path, self.filelist[self.data_index])
            filelist.append(self.filelist[self.data_index])
            ################
            greyimg, colorimg = self.read_img_grav(filename)
            #greyimg, colorimg = filterGrav.gravurLike(filename)
            #################
            batch.append(greyimg)
            labels.append(colorimg)
            self.data_index = (self.data_index + 1) % self.size
        batch = np.asarray(batch)/255
        labels = np.asarray(labels)/255
        return batch, labels, filelist
