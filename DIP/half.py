# -*- coding = utf-8 -*-
# @Time : 2021/8/1 12:53
# @Author : 水神与月神
# @File : half.py
# @Software : PyCharm

import cv2 as cv
import os


def half(read_path, save_path):
    """
    批量处理图片，只要图片的下半部分，之后可能会加上别的half方式
    :param read_path:读取图片的文件夹
    :param save_path:保存图片的文件夹
    :return:没有返回值，直接将处理好的图片，保存在想要的路径
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    file_names = os.listdir(read_path)
    for file_name in file_names:
        read = os.path.join(read_path, file_name)
        save = os.path.join(save_path, file_name)
        try:
            f = cv.imread(read, cv.IMREAD_UNCHANGED)
            w = f[1002:, :]
            cv.imwrite(save, w)
            print("图片{:s}保存成功！".format(save))
        except TypeError:
            print('图片{:s}格式有问题'.format(read))


if __name__ == '__main__':
    path_read = r'C:\Users\dell\Desktop\001'
    path_save = r'C:\Users\dell\Desktop\half'
    half(path_read, path_save)


