from PIL import Image
import numpy as np


def image_input(img_path, dim=(200, 200)):
    img = Image.open(img_path)
    img_new = crop_center(img)
    return np.asarray(img_new.resize((200, 200), Image.ANTIALIAS))
    # return cv2.resize(img_arr, dim, interpolation=cv2.INTER_AREA)


def crop_center(img, size=(300, 300)):
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img_new = img.crop(
        (
            half_the_width - size[0]/2,
            half_the_height - size[1]/2,
            half_the_width + size[0]/2,
            half_the_height + size[1]/2
        )
    )
    return img_new
