from PIL import Image
import numpy as np
import image_operation

img = Image.open(
    "/media/tabul/DATA/!LIPI/Wood-Classification-Server/static/USER_IMAGE/cd395db2-6646-402a-a6ea-dfba45e36e15.png")
# img = img.resize((200, 200), Image.ANTIALIAS)
img_new = image_operation.crop_center(img)
img_new = img_new.resize((200, 200), Image.ANTIALIAS)
img_new.save('resized_image.jpg')
