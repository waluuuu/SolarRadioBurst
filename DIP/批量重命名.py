# -*- coding = utf-8 -*-
# @Time : 2021/8/16 17:59
# @Author : 水神与月神
# @File : 批量重命名.py
# @Software : PyCharm


import os
import cv2 as cv

path = r'C:\Users\dell\Desktop\process'
save = r'C:\Users\dell\Desktop\process2'

filenames = os.listdir(path)
count = 0
for filename in filenames:
    count += 1
    new_name = r'test2_{:d}.png'
    image = cv.imread(os.path.join(path, filename), cv.IMREAD_UNCHANGED)
    print(1)
    cv.imwrite(os.path.join(save, new_name.format(count)), image)
    print("图片保存完成{:s}".format(filename))
