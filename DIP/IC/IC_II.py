# -*- coding = utf-8 -*-
# @Time : 2021/6/16 20:05
# @Author : 水神与月神
# @File : IC_II.py
# @Software : PyCharm


import os
import cv2 as cv

read = r'G:\test\normal_x\typeII\O'
save = r'G:\test\normal_x\typeII\reshape'

filenames = os.listdir(read)

for filename in filenames:
    image = cv.imread(os.path.join(read, filename), cv.IMREAD_UNCHANGED)
    width = image.shape[1]
    if width < 300 :
        continue

    n = width // 400
    if width % 400 >300:
        n += 1
    use = width // n
    for i in range(n):
        temp = image[:, i * use:(i + 1) * use]
        cv.imwrite(os.path.join(save, filename.split(".")[0] + "{:d}.png".format(i)), temp)
        print(filename.split(".")[0] + "{:d}.png".format(i) + "已保存")


