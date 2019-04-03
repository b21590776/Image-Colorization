
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
import data as data
import model as model
import config as config
import datetime



if __name__ == "__main__":
    with open(os.path.join(config.LOG_DIR, str(datetime.datetime.now().strftime("%Y%m%d")) + "_" + str(config.BATCH_SIZE)
                                           + "_" + str(config.NUM_EPOCHS) + ".txt"), "w") as log:
        log.write(str(datetime.datetime.now()) + "\n")
        log.write("Use Pretrained Weights: " + str(config.USE_PRETRAINED) + "\n")
        log.write("Pretrained Model: " + config.PRETRAINED + "\n")


        # READ DATA
        train_data = data.DATA("/content/drive/My Drive/colorization_tensorflow/DATASET/Gravur/data")
        print("Train Data Loaded")


        # BUILD MODEL
        model = model.MODEL()
        print("Model Initialized")
        model.build()
        print("Model Built")


        # TRAIN MODEL
        model.train(train_data, log)
        print("Model Trained")


        #test_gravur
        #data_test

        """
        # TEST MODEL
        test_data = data.DATA("/content/drive/My Drive/colorization_tensorflow/DATASET/Gravur/specific_test")
        print("Test Data Loaded")
        model.test(test_data, log)
        print("Image Reconstruction Done")
        """



