import cv2
import numpy as np
from keras.models import load_model
from keras.applications import MobileNet
from app import APP_ROOT
from keras.utils.generic_utils import CustomObjectScope
import keras, image_operation
from keras.optimizers import Adam
from keras import losses
import numpy as np

# with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6,'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
#     model = load_model(APP_ROOT + "/static/saved_models/MobileNet_wood_model.hdf5")

model = MobileNet(include_top=True, weights=None, classes=2, pooling='max', input_shape=(200, 200, 3))
model.load_weights(APP_ROOT + "/static/saved_models/1_MobileNet_wood_weight.hdf5")


def predict_class(img_input):
    print("path: " + img_input)
    hasil = model.predict(np.expand_dims(image_operation.image_input(APP_ROOT + "\\" + img_input),axis=0))
    print(hasil)