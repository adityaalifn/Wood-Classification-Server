from PIL import Image
import numpy as np
import cv2

def image_input(img_path,dim=(200,200)):
    img = Image.open(img_path)
    img = img.convert("RGB")
    img_arr = np.asarray(img)
    return cv2.resize(img_arr, dim, interpolation=cv2.INTER_AREA)