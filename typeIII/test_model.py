# -*- coding = utf-8 -*-
# @Time : 2021/6/10 19:39
# @Author : 水神与月神
# @File : test_model.py
# @Software : PyCharm

from keras.models import load_model
import numpy as np
from keras.preprocessing import image

III_dir = r'G:\test\normal_x\typeIII\val\III'
O_dir = r'G:\test\normal_x\typeIII\val\O'

model = load_model(r'F:\SolarRadioBurst\typeIII\typeIII_binary_normalization_100_1.3_50.h5')

# def my_image(path):
#     out = []
#     filenames = os.listdir(path)
#     for filename in filenames:
#         image = cv.imread(os.path.join(path, filename))
#
#         image = cv.resize(image, (400, 100))
#         image = image/255.0
#         out.append(image)
#     return np.array(out)
#
# imgs_III = my_image(III_dir)
# imgs_O = my_image(O_dir)
# ret_III = model.predict_classes(imgs_III)
# ret_O = model.predict_classes(imgs_O)

# ret_III = model.predict(imgs_III)
# ret_O = model.predict(imgs_O)
# print(ret_O)

# ret_III = ret_III.tolist()
# ret_O = ret_O.tolist()
# true = ret_III.count([0])
# false = ret_O.count([0])
# TPR = true/len(ret_III)
# FPR = false/len(ret_O)
# print("TPR is :{:f} ".format(TPR))
# print("FPR is :{:f} ".format(FPR))

path = r'F:\SolarRadioBurst\ProjectDemo\img.png'

# image = cv.imread(path)
# # image = demo.normalization_x(image)
# image = cv.resize(image, (400, 100))
#
# image = image / 255.0
#
# out = []
# out.append(image)
# result = model.predict_classes(image)


img = image.load_img(path, target_size=(400, 100))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
img_tensor /= 255.

result = model.predict(img_tensor)
print(result)
