# -*- coding = utf-8 -*-
# @Time : 2021/7/16 19:56
# @Author : 水神与月神
# @File : DisplayResult.py
# @Software : PyCharm


"""
分割出来的图片，有的明显看不到爆发，有的有其它类型的爆发（比较强的二型爆）
尝试先归一化，再直方图均衡后，能不能清楚的看到
"""
import os
import numpy as np
import cv2 as cv
from DIP.Normal import Normal
from matplotlib import pyplot as plt
from DIP.show import show

# path_read = r'G:\LearmonthData\IVN'
# path_write = r'G:\LearmonthData\IVNE'
#
# for root, dirs, files in os.walk(path_read, topdown=False):
#     for name in files:
#         image = cv.imread(os.path.join(root, name), cv.IMREAD_UNCHANGED)
#         new = Normal(image)
#         img = new.process(method="NORMAL_Z")
#         img = cv.equalizeHist(img)
#         pp = os.path.join(path_write, root.split('\\')[-1], name)
#         cv.imwrite(pp, img)
#         print('已经保存')


# 绘制图片的灰度直方图
# path_read = r'G:\LearmonthData\IV'
# path_write = r'G:\LearmonthData\IVH'
#
# for root, dirs, files in os.walk(path_read, topdown=False):
#     for name in files:
#         img = cv.imread(os.path.join(root, name), cv.IMREAD_UNCHANGED)
#         plt.hist(img.ravel(), 256, [0, 256])
#         pp = os.path.join(path_write, root.split('\\')[-1], name)
#         plt.savefig(pp)
#         plt.close()
#         print('已经保存')


# 开始尝试下采样

# path_read = r'G:\LearmonthData\IVS'
# path_write = r'G:\LearmonthData\IVNED'
#
# for root, dirs, files in os.walk(path_read, topdown=False):
#     for name in files:
#         img = cv.imread(os.path.join(root, name), cv.IMREAD_UNCHANGED)
#         out = cv.resize(img, (150, 150))
#         pp = os.path.join(path_write, root.split('\\')[-1], name)
#         cv.imwrite(pp, out)
#         print('已经保存')

# 测试普通图片resize之后的效果
path = r'G:\LearmonthData\learmonth_pics\2007\LM070104.srs.png'
image = cv.imread(path, cv.IMREAD_UNCHANGED)

new = Normal(image)
temp = new.process(method="NORMAL_Z")
img = cv.equalizeHist(temp)

out = cv.resize(img, (150, 150))

show('dd', out)
