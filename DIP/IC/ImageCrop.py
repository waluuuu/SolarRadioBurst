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
"""

import os
import cv2 as cv

read = r'G:\test\normal_x\typeIII1.2\O'
save = r'G:\test\normal_x\typeIII1.2\reshape'

filenames = os.listdir(read)

for filename in filenames:
    image = cv.imread(os.path.join(read, filename), cv.IMREAD_UNCHANGED)
    width = image.shape[1]
    n = width // 200
    if width % 200 > 150:
        n += 1
    use = width // n
    for i in range(n):
        temp = image[:, i * use:(i + 1) * use]
        cv.imwrite(os.path.join(save, filename.split(".")[0] + "{:d}.png".format(i)), temp)
        print(filename.split(".")[0] + "{:d}.png".format(i) + "已保存")


