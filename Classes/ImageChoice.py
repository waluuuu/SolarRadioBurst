# -*- coding = utf-8 -*-
# @Time : 2021/7/29 9:35
# @Author : 水神与月神
# @File : ImageChoice.py
# @Software : PyCharm
# 这是用来制作数据集的，从分割好的图片中，随机选取图片制作训练用的数据集
# 按照7：3制作的
import os
import shutil
import random


class ImageChoice:
    def __init__(self, path_read, path_write):
        # 读取路径
        self._path_read = path_read
        # 保存路径，保存训练集和验证集
        self._path_write = path_write
        # 每种类型，训练集和验证集数目
        self._num = {'2L': [240, 100], '3': [500, 210], '4': [500, 210], 'cont': [500, 210],
                     'calibration': [250, 110], 'noburst': [1490, 620]}
        # 每种类型的二级目录
        self._sub_directory = ['2L 340', '3 1387', '4 1145', 'calibration 363', 'cont 1881', 'noburst 2129']

    def action(self):
        for sub_dir in self._sub_directory:
            # 列出每一类的所有文件名
            filenames = os.listdir(os.path.join(self._path_read, sub_dir))
            # 查看这种类型有多少张
            num_range = range(0, len(filenames))
            # 查看这种类型一共需要多少张
            num = self._num[sub_dir.split(' ')[0]][0] + self._num[sub_dir.split(' ')[0]][1]
            # 随机选出我们需要数目个索引
            ran = random.sample(num_range, num)

            # 制作训练集
            for i in ran[0: self._num[sub_dir.split(' ')[0]][0]]:
                filename = filenames[i]
                # 判断是不是爆发，分别存储到不同的文件夹中
                if sub_dir != 'calibration 363' and sub_dir != 'noburst 2129':
                    sub_dir_write = 'train/B'
                else:
                    sub_dir_write = 'train/N'
                # 将图片复制到新的文件夹
                shutil.copy(os.path.join(self._path_read, sub_dir, filename),
                            os.path.join(self._path_write, sub_dir_write, filename))
                print('图片{:s}已保存'.format(filename))

            # 制作验证集
            for i in ran[self._num[sub_dir.split(' ')[0]][0]:]:
                filename = filenames[i]
                # 判断是不是爆发
                if sub_dir != 'calibration 363' and sub_dir != 'noburst 2129':
                    sub_dir_write = 'val/B'
                else:
                    sub_dir_write = 'val/N'
                # 将图片复制到新的文件夹
                shutil.copy(os.path.join(self._path_read, sub_dir, filename),
                            os.path.join(self._path_write, sub_dir_write, filename))
                print('图片{:s}已保存'.format(filename))
