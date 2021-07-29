# -*- coding = utf-8 -*-
# @Time : 2021/6/13 16:09
# @Author : 水神与月神
# @File : ImageCrop.py
# @Software : PyCharm

"""
网络实际使用效果不好，推测是由于训练用的数据和实际使用的数据大小不一样
训练用的数据被压缩之后传入，压缩比例比实际的要高
所以，把其它类型的爆发的尺寸变成和三型爆尺寸相同
应该可以更加实用

再次修改这个文件，将各类图片都分割一下，，变成和III型爆差不多大，然后再筛选。
如果可以的话，再多筛选一些III型爆
"""

import os
import cv2 as cv

# 文件读取路径和保存路径


path_read = r'G:\useful_L\calibration'
path_save = r'G:\useful_L\reshape\calibration'

filenames = os.listdir(path_read)

for filename in filenames:
    image = cv.imread(os.path.join(path_read, filename), cv.IMREAD_UNCHANGED)
    width = image.shape[1]
    n = width // 200
    if width % 200 > 150:
        n += 1
    new_length = width // n
    for i in range(n):
        temp = image[:, i * new_length:(i + 1) * new_length]
        cv.imwrite(os.path.join(path_save, filename.split(".")[0] + "{:d}.png".format(i)), temp)
        print(filename.split(".")[0] + "{:d}.png".format(i) + "已保存")


