from PIL import Image
import numpy as np


def image_input(img_path, dim=(200, 200)):
    img = Image.open(img_path)
    return np.asarray(img.resize((200, 200), Image.ANTIALIAS))
    # return cv2.resize(img_arr, dim, interpolation=cv2.INTER_AREA)
