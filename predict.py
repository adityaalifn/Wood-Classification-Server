from keras import models
import image_operation
import numpy as np
import h5py

def predict_class(img_input):
    model = models.load_model("./static/xceptionMobile_wood_model.h5")
    # print("path: " + img_input)
    #print(np.shape(np.expand_dims(image_operation.image_input(APP_ROOT + "/" + img_input), axis=0)))
    img = np.expand_dims(image_operation.image_input(img_input), axis=0)
    hasil = model.predict(img)
    # print(hasil)
    if(hasil[0][0] > hasil[0][1]):
        return '0'
    else:
        return '1'
