# -*- coding = utf-8 -*-
# @Time : 2021/8/7 0:00
# @Author : 水神与月神
# @File : test.py
# @Software : PyCharm


import cv2 as cv


def show(path):
    image = cv.imread(path, cv.IMREAD_UNCHANGED)
    image2 = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    cv.imshow('name', image2)
    cv.waitKey()
    cv.destroyWindow('name')
