# -*- coding = utf-8 -*-
# @Time : 2021/6/19 16:09
# @Author : 水神与月神
# @File : show.py
# @Software : PyCharm
# 中期报告时用来生成展示用的图片，包含了所有的方法
# %%
from Classes.Normal import Normal
from show import show
import cv2 as cv
import numpy as np

# %% ------------读取图片-------------
r"G:\LearmonthData\New\III\LM200102240110_III_25_180.jpg"
path = r'G:\useful_L\2\CG199711030433_FN,H_30_130.jpg.jpg'
image = cv.imread(path)

# %% --------------彩色图片转灰度图片------------------
image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

# %% ------------通道归一化------------------------
process = Normal(image)
show("show", process.process("NORMAL_X"))

# %% ------------自适应二值化------------------------
binary_img = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)
show("show", binary_img)

# %% -----------canny边缘检测----------------------
canny_low = 40
canny_high = 50
edge = cv.Canny(image, canny_low, canny_high)
show("show", edge)

# %% -----------图像形态学-------------------------
# 配合别的方法使用，比如自适应二值化之后，使用
kernel_1_10 = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))
kernel_4_15 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (4, 15), (-1, -1))
dst = cv.erode(binary_img, kernel_1_10)  # 水平方向
# dst2 = cv.dilate(dst, kernel_4_15)  # 水平方向
images = np.hstack([binary_img, dst])
show("show", images)

# %%----------------直方图均衡----------------
image_e = cv.equalizeHist(image)
show("show", image_e)

