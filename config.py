import os

class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    BASEPATH = os.path.dirname(__file__)
    IMAGE_UPLOAD_LOCATION = os.path.join(BASEPATH, 'data/input_image', 'input.jpg')
    MODEL_NAME = 'VGG'
    NO_OF_SIMILAR_IMAGES = 4
    DATASET = 'my_dataset'
    #DATASET_IMAGES_PATH = os.path.join(BASEPATH, 'data/dataset', DATASET)
    DATASET_IMAGES_PATH = os.path.join('app/static', 'images')
    MODEL_PATH = os.path.join(BASEPATH, 'data/models', 'model.h5')
