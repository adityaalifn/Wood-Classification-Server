from keras.applications import MobileNet
from app import APP_ROOT
import keras
import image_operation
import numpy as np
import h5py


def predict_class(img_input):
    model = MobileNet(include_top=True, weights=None, classes=2,
                      pooling='max', input_shape=(200, 200, 3))
    model.load_weights(APP_ROOT + "/static/1_MobileNet_wood_weight.hdf5")
    print("path: " + img_input)
    print(np.shape(np.expand_dims(image_operation.image_input(
        APP_ROOT + "/" + img_input), axis=0)))
    img = np.expand_dims(image_operation.image_input(
        APP_ROOT + "/" + img_input), axis=0)
    hasil = model.predict(img)
    print(hasil)
    if(hasil[0][0] > hasil[0][1]):
        return '0'
    else:
        return '1'
