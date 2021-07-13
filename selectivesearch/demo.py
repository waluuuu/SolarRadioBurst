# -*- coding = utf-8 -*-
# @Time : 2021/6/2 19:39
# @Author : 水神与月神
# @File : demo.py
# @Software : PyCharm


import selectivesearch
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# %%

def normalization_x(filename):
    # 徐龙老师采用的消除横线噪声的通道归一化方法
    image = filename.copy()
    # list 没有shape方法
    shape = image.shape
    global_mean = np.mean(image)
    # 防止255溢出，先将数组转换成列表
    image = image.tolist()
    for i in range(shape[0]):
        channel_mean = np.mean(image[i])
        image[i] = image[i] - channel_mean + global_mean
    image = np.array(image, dtype=np.uint8)
    return image


# %%
path = r'F:\SolarRadioBurst\selectivesearch\LM200811030030_IIIs_25_180.jpg'
image = cv.imread(path, cv.IMREAD_UNCHANGED)
image = normalization_x(image)
image = cv.equalizeHist(image)

# cv.imshow("image", image)
# cv.waitKey()
# cv.destroyWindow("image")
#
# 参考链接：https://blog.csdn.net/jsond/article/details/74923089

image = cv.cvtColor(image,cv.COLOR_GRAY2RGB)
img_lbl, regions = selectivesearch.selective_search(image, scale=10, sigma=0.8, min_size=200)


# fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
# ax.imshow(image)
# for reg in regions:
#     x, y, w, h = reg['rect']
#     rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
#     ax.add_patch(rect)
# plt.show()




# %%
# 接下来我们把窗口和图像打印出来，对它有个直观认识
# fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
# ax.imshow(image)
# for reg in regions:
#     x, y, w, h = reg['rect']
#     rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
#     ax.add_patch(rect)
# plt.show()

candidates = []

for i in regions:
    if i['rect'] in candidates:
        continue
    x, y, w, h = i['rect']
    if w == 0 or h == 0:
        continue
    else:
        if w / h > 3:
            continue
        else:
            if w*h < 500:
                continue
    if h/w < 1 :
        continue

    if h*w < 800:
        continue
    candidates.append((x, y, w, h))

# l = len(candidates)
# print('len====', l)
# 3)对过滤完的窗口进行展示
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))
ax.imshow(image)
for x, y, w, h in candidates:
    rect = mpatches.Rectangle(
        (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
    ax.add_patch(rect)
plt.show()

# 筛选条件
# 长宽比非常大
# 长宽比正常。但是面积比较小
# 面积比较小，长度比较短
# 过滤掉重复，过滤掉大圈套小圈
