# -*- coding = utf-8 -*-
# @Time : 2021/8/9 20:05
# @Author : 水神与月神
# @File : 选择图片.py
# @Software : PyCharm


import os
import shutil
import random


def action(path_read, path_train, path_val, path_test):
    filenames = os.listdir(path_read)
    # 查看这种类型有多少张
    num_range = range(0, len(filenames))
    # 查看这种类型一共需要多少张
    num = 431
    # 随机选出我们需要数目个索引
    ran = random.sample(num_range, num)

    # 制作训练集
    for i in ran[0: 259]:
        filename = filenames[i]
        # 将图片复制到新的文件夹
        shutil.copy(os.path.join(path_read, filename), os.path.join(path_train, filename))
        print('图片{:s}已保存'.format(filename))

    # 制作验证集
    for i in ran[259: 345]:
        filename = filenames[i]
        # 将图片复制到新的文件夹
        shutil.copy(os.path.join(path_read, filename), os.path.join(path_val, filename))
        print('图片{:s}已保存'.format(filename))

    # 制作测试集
    for i in ran[345: 431]:
        filename = filenames[i]
        # 将图片复制到新的文件夹
        shutil.copy(os.path.join(path_read, filename), os.path.join(path_test, filename))
        print('图片{:s}已保存'.format(filename))


if __name__ == '__main__':
    read = r'G:\useful_C\test_C\normal3\N'
    train = r'G:\useful_C\test_C\normal3\test\train\N'
    val = r'G:\useful_C\test_C\normal3\test\val\N'
    test = r'G:\useful_C\test_C\normal3\test\test\N'
    action(read, train, val, test)
