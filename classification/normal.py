# -*- coding = utf-8 -*-
# @Time : 2021/8/3 22:59
# @Author : 水神与月神
# @File : normal.py
# @Software : PyCharm

# %%

import os
import cv2 as cv
import numpy as np


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


def normalization_z(filename):
    # 张沛锦采用的消除背景缓变噪声的通道归一化方法
    img = filename.copy()
    # list 没有shape方法
    shape = img.shape
    # 防止255溢出，先将数组转换成列表
    image = img.tolist()

    for i in range(shape[0]):
        channel_mean = np.mean(image[i])
        image[i] = abs(image[i] - channel_mean)
    image = np.array(image, dtype=np.uint8)
    return image


# %%


#train_path_II = r'G:\useful_L\NEW_NET_3.0\train\II'
# train_path_III = r'G:\useful_L\NEW_NET_3.0\train\III'
# train_path_B = r'G:\useful_L\NEW_NET_2.1\train\B'
# train_path_N = r'G:\useful_L\NEW_NET_2.1\train\N'
# # train_path_O = r'G:\useful_L\NEW_NET_3.0\train\O'
# #val_path_II = r'G:\useful_L\NEW_NET_3.0\val\II'
# # val_path_III = r'G:\useful_L\NEW_NET_3.0\val\III'
# val_path_B = r'G:\useful_L\NEW_NET_2.1\val\B'
# val_path_N = r'G:\useful_L\NEW_NET_2.1\val\N'
# # val_path_O = r'G:\useful_L\NEW_NET_3.0\val\O'
#
#
#
# #train_save_II = r'G:\useful_L\Normal2\NEW_NET_3.0\train\II'
# # train_save_III = r'G:\useful_L\Normal2\NEW_NET_3.0\train\III'
# train_save_B = r'G:\useful_L\Normal\NEW_NET_2.1\train\B'
# train_save_N = r'G:\useful_L\Normal\NEW_NET_2.1\train\N'
# #train_save_O = r'G:\useful_L\Normal2\NEW_NET_3.0\train\O'
# #val_save_II = r'G:\useful_L\Normal2\NEW_NET_3.0\val\II'
# #val_save_III = r'G:\useful_L\Normal2\NEW_NET_3.0\val\III'
# val_save_B = r'G:\useful_L\Normal\NEW_NET_2.1\val\B'
# val_save_N = r'G:\useful_L\Normal\NEW_NET_2.1\val\N'
# #val_save_O = r'G:\useful_L\Normal2\NEW_NET_3.0\val\O'
#
# # 二维数组，存储读取文件夹和保存文件夹
# # path_s = [[train_path_II, train_save_II], [train_path_III, train_save_III], [train_path_N, train_save_N],
# #           [train_path_O, train_save_O],
# #           [val_path_II, val_save_II], [val_path_III, val_save_III], [val_path_N, val_save_N], [val_path_O, val_save_O]
# #           ]
#
# path_s = [[train_path_B, train_save_B], [train_path_N, train_save_N],
#           [val_path_B, val_save_B], [val_path_N, val_save_N]
#           ]

path_II = r'G:\useful_C\test_C\II'
path_III = r'G:\useful_C\test_C\III'
path_N = r'G:\useful_C\test_C\N'
path_O = r'G:\useful_C\test_C\O'

save_II = r'G:\useful_C\test_C\normal2\II'
save_III = r'G:\useful_C\test_C\normal2\III'
save_N = r'G:\useful_C\test_C\normal2\N'
save_O = r'G:\useful_C\test_C\normal2\O'

# 二维数组，存储读取文件夹和保存文件夹
path_s = [[path_II, save_II], [path_III, save_III], [path_N, save_N], [path_O, save_O]]
# %%

for i in path_s:
    path_read = i[0]
    path_save = i[1]
    if os.path.exists(path_save):
        pass
    else:
        os.mkdir(path_save)

    file_names = os.listdir(path_read)

    for file_name in file_names:
        full_path_read = os.path.join(path_read, file_name)
        full_path_save = os.path.join(path_save, file_name)
        if os.path.exists(full_path_save):
            continue
        image = cv.imread(full_path_read, cv.IMREAD_UNCHANGED)
        # image2 = normalization_z(image)
        image2 = normalization_z(image)
        cv.imwrite(full_path_save, image2)
        print("图片{:s}保存完毕".format(file_name))

