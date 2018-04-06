from PIL import Image
import numpy as np
basewidth = 200
img = Image.open("/media/tabul/DATA/!LIPI/Wood-Classification-Server/static/USER_IMAGE/cc92d58d-6af9-4501-b861-8bbadc5fa90b.jpg")
img = img.resize((200, 200), Image.ANTIALIAS)
print(np.asfarray(img))
print(np.asfarray(img).shape)
img.save('resized_image.jpg')