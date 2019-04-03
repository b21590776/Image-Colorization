import os

# DIRECTORY INFORMATION
DATASET = "Gravur"
ROOT_DIR = os.path.abspath('/content/drive/My Drive/colorization_tensorflow')
DATA_DIR = os.path.join(ROOT_DIR, 'DATASET/'+DATASET+'/')
OUT_DIR = os.path.join(ROOT_DIR, 'RESULT/'+DATASET+'/')
MODEL_DIR = os.path.join(ROOT_DIR, 'MODEL/')
LOG_DIR = os.path.join(ROOT_DIR, 'LOGS/'+DATASET+'/')

TRAIN_DIR = "train"
TEST_DIR = "portreler"

# DATA INFORMATION
IMAGE_SIZE = 224
BATCH_SIZE = 2

# RANDOM NUMBER GENERATOR INFORMATION
SEED = 128

# TRAINING INFORMATION
USE_PRETRAINED = True
PRETRAINED = "model2_30.ckpt"
NUM_EPOCHS = 30
