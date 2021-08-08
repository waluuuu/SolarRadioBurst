# -*- coding = utf-8 -*-
# @Time : 2021/8/2 23:13
# @Author : 水神与月神
# @File : RowToImg.py
# @Software : PyCharm


import os
import numpy as np
import cv2 as cv


# %%
# 这个函数用来按字节读取数据，num为读取的字节的个数，bytestream是打开的文件

def read_uint_num(bytestream, num):
    dt = np.dtype(np.uint8)  # 读取字节
    return np.frombuffer(bytestream.read(num), dtype=dt)


# %%
# 这个函数用来生成文件


def my_read(fileName):
    array = []
    with open(fileName, "rb") as f:
        while True:
            discard24uint8 = read_uint_num(f, 40)
            needed = read_uint_num(f, 2004)
            if len(needed) == 0:
                break
            needed = needed[::-1]
            array.append(needed)

    array = np.concatenate(array, axis=0)
    dt = np.dtype(np.uint8)
    ndarray = np.array(array, dtype=dt)
    try:
        ndarray = ndarray.reshape(-1, 2004)
    except ValueError as e:
        print("图片转换失败！")

    ndarray = np.transpose(ndarray)
    ndarray = ndarray.astype(np.uint8)
    return ndarray


def save(name_read, save_path_root, path_save, name_save):
    path_names = os.listdir(save_path_root)
    if path_save in path_names:
        pass
    else:
        os.makedirs(os.path.join(save_path_root, path_save))

    out = my_read(name_read)
    lf = os.path.join(os.path.join(save_path_root, path_save), name_save)
    cv.imwrite(lf + ".png", out)


if __name__ == '__main__':
    read_path = r'C:\Users\dell\Desktop\新建文件夹'
    save_path = r'C:/Users/dell/Desktop/'
    filenames = os.listdir(read_path)
    for filename in filenames:
        save(os.path.join(read_path, filename), save_path, '001', filename)

