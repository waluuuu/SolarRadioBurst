# -*- coding = utf-8 -*-
# @Time : 2021/7/13 10:16
# @Author : 水神与月神
# @File : 图片批处理.py
# @Software : PyCharm

import os
import cv2 as cv

path_read = r''
path_write = r''

filenames = os.listdir(path_read)

for filename in filenames:
    image = cv.imread(filename, cv.IMREAD_UNCHANGED)

    """使用不同的数字图像处理方法，从methods里面找，这里以直方图均衡为例"""
    image = cv.equalizeHist(image)

    cv.imwrite(os.path.join(path_write, filename), image)


