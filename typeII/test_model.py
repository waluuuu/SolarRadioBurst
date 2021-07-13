# -*- coding = utf-8 -*-
# @Time : 2021/6/18 15:21
# @Author : 水神与月神
# @File : test_model.py
# @Software : PyCharm

from DIP.ImageProcess import ImageProcess
from TestModel import TestModel
import cv2 as cv

model_path = r"F:\SolarRadioBurst\typeII\typeII_binary_normalization_50_1.1.h5"
image_path = r"G:\useful_L\2\CG199510130502_FN_25_220.jpg.jpg"
model = TestModel(model_path)
image = ImageProcess(cv.imread(image_path), (400, 200)).image_in("NORMAL_X")
print(model.predict(image))


