from image_operation import image_input
import numpy as np
import keras
from keras.applications import MobileNet
from keras.models import load_model
from keras.utils.generic_utils import CustomObjectScope

with open("./static/species_list.txt", "r") as file:
    species_list = file.read()
    species_list = species_list.replace(
        "[", "").replace("]", "").replace("'", "").split(",")


def predict_class(img_input):
    # model = MobileNet(include_top=True, weights=None, classes=8,
    #                   pooling='max', input_shape=(200, 200, 3))
    # model.load_weights("./static/MobileNet_wood_model_new.hdf5")
    with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6, 'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
        model = load_model("./static/MobileNet_wood_model_new.hdf5")
    # print("path: " + img_input)
    #print(np.shape(np.expand_dims(image_operation.image_input(APP_ROOT + "/" + img_input), axis=0)))
    img = np.expand_dims(image_input(img_input), axis=0)
    hasil = model.predict(img)
    # print(hasil)
    result = hasil.argmax()
    del model
    return species_list[result]
