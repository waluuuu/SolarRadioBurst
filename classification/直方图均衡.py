# -*- coding = utf-8 -*-
# @Time : 2021/8/7 23:00
# @Author : 水神与月神
# @File : 直方图均衡.py
# @Software : PyCharm


import os
import cv2 as cv

# path_II = r'G:\useful_C\test_C\normal2\II'
# path_III = r'G:\useful_C\test_C\normal2\III'
# path_N = r'G:\useful_C\test_C\normal2\N'
# path_O = r'G:\useful_C\test_C\normal2\O'
#
# save_II = r'G:\useful_C\test_C\normal3\II'
# save_III = r'G:\useful_C\test_C\normal3\III'
# save_N = r'G:\useful_C\test_C\normal3\N'
# save_O = r'G:\useful_C\test_C\normal3\O'
#
# # 二维数组，存储读取文件夹和保存文件夹
# path_s = [[path_II, save_II], [path_III, save_III], [path_N, save_N], [path_O, save_O]]

II = r'G:\useful_L\Normal2\NEW_NET_4.0\train\II'
III = r'G:\useful_L\Normal2\NEW_NET_4.0\train\III'
N = r'G:\useful_L\Normal2\NEW_NET_4.0\train\N'
O = r'G:\useful_L\Normal2\NEW_NET_4.0\train\O'
V_II = r'G:\useful_L\Normal2\NEW_NET_4.0\val\II'
V_III = r'G:\useful_L\Normal2\NEW_NET_4.0\val\III'
V_N = r'G:\useful_L\Normal2\NEW_NET_4.0\val\N'
V_O = r'G:\useful_L\Normal2\NEW_NET_4.0\val\O'

s_II = r'G:\useful_L\Normal3\NEW_NET_4.0\train\II'
s_III = r'G:\useful_L\Normal3\NEW_NET_4.0\train\III'
s_N = r'G:\useful_L\Normal3\NEW_NET_4.0\train\N'
s_O = r'G:\useful_L\Normal3\NEW_NET_4.0\train\O'
s_V_II = r'G:\useful_L\Normal3\NEW_NET_4.0\val\II'
s_V_III = r'G:\useful_L\Normal3\NEW_NET_4.0\val\III'
s_V_N = r'G:\useful_L\Normal3\NEW_NET_4.0\val\N'
s_V_O = r'G:\useful_L\Normal3\NEW_NET_4.0\val\O'


path_s = [[II, s_II], [III, s_III], [N, s_N], [O, s_O], [V_II, s_V_II], [V_III, s_V_III], [V_N, s_V_N], [V_O, s_V_O]]

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
        try:
            dst = cv.equalizeHist(image)
            cv.imwrite(full_path_save, dst)
            print("图片{:s}保存完毕".format(file_name))
        except cv.error:
            pass
