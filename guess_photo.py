import base64
from PIL import Image
import numpy as np
import os


def readphoto(imgstring):
    imgdata = base64.b64decode(imgstring)
    filename = "Some_image.jpg"  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
        # fh.write(base64.decodebytes(img_data))
        f.close()
    print("image loaded sucessfully")




#convert image tonumpy array
def convert_img_to_numpy(img_name):
    img = Image.open(img_name).convert('L') #convert image to gray scale
    img.thumbnail((28,28)) #resize image 28*28
    #convert the image tonumpy array
    arr = np.array(img.getdata(), dtype=np.uint8)
    field = np.resize(arr, (img.size[1], img.size[0]))
    out = field
    return out
   # img = Image.fromarray(out, mode='L')
   # img.show()#plotimage

#deletephoto after prediction
def delete_photo(image_name):
        os.remove(image_name)


#predict image
def predict_image(numpy_array):
    pass



