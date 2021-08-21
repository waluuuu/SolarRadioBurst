# -*- coding = utf-8 -*-
# @Time : 2021/8/1 13:18
# @Author : 水神与月神
# @File : length_filter.py
# @Software : PyCharm
# 将长度不符合的图片剔除

import cv2 as cv
import os


def length(read_path):
    """
    将文件夹中不符合大小要求的爆发类型删除
    """
    file_names = os.listdir(read_path)
    for file_name in file_names:
        read = os.path.join(read_path, file_name)
        try:
            f = cv.imread(read, cv.IMREAD_UNCHANGED)
            shape = f.shape
            if shape[1] <= 250:
                pass
            else:
                os.remove(read)
        except TypeError:
            print('图片{:s}格式有问题'.format(read))


if __name__ == '__main__':
    path_read = r'C:\Users\dell\Desktop\half'
    length(path_read)
