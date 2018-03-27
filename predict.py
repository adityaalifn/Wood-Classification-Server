from keras.models import load_model
import cv2
import numpy as np

model = load_model("./static/saved_models/1_MobileNet_wood_weight.hdf5")

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
