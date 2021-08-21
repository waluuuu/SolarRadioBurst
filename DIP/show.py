# -*- coding = utf-8 -*-
# @Time : 2021/7/13 11:04
# @Author : 水神与月神
# @File : show.py
# @Software : PyCharm
# 同时展示多张图片
# 要求输入名称和多张图片的np.hstack

import cv2 as cv


def show(name, image):
    cv.imshow(name, image)
    cv.waitKey()
    cv.destroyWindow(name)
