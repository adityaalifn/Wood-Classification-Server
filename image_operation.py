from PIL import Image
import numpy as np


def image_input(img_path, dim=(200, 200)):
    img = Image.open(img_path)
    img = img.convert("RGB")
    img_arr = np.asarray(img)
    size = 200, 200
    return np.asarray(img.thumbnail(size, Image.ANTIALIAS))
    # return cv2.resize(img_arr, dim, interpolation=cv2.INTER_AREA)
