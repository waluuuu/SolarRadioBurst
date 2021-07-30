# -*- coding = utf-8 -*-
# @Time : 2021/7/29 16:53
# @Author : 水神与月神
# @File : 训练集3.0.py
# @Software : PyCharm

# 这次从二分类中加了III型爆，变成了三分类，用3.0来命名
# 由于有较大偏差，需要重写ImageChoice类的方法

import os
import shutil
import random
from Classes.ImageChoice import ImageChoice


class ImageChoice2(ImageChoice):
    def __init__(self, path_read, path_write):
        # 读取路径
        super().__init__(path_read, path_write)
        # 每种类型，训练集和验证集数目
        self._num = {'2noIII': [200, 60], '3': [1000, 300], '4': [400, 120], 'contnoIII': [400, 120],
                     'calibration': [250, 110], 'noburst': [750, 190]}
        # 每种类型的二级目录
        self._sub_directory = ['2noIII', '3 1387', '4 1145', 'calibration 363', 'contnoIII', 'noburst 1998']

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
                if sub_dir == 'calibration 363' or sub_dir == 'noburst 1998':
                    sub_dir_write = 'train/noburst'
                elif sub_dir == '3 1387':
                    sub_dir_write = 'train/III'
                else:
                    sub_dir_write = 'train/other'

                # 将图片复制到新的文件夹
                shutil.copy(os.path.join(self._path_read, sub_dir, filename),
                            os.path.join(self._path_write, sub_dir_write, filename))
                print('图片{:s}已保存'.format(filename))

            # 制作验证集
            for i in ran[self._num[sub_dir.split(' ')[0]][0]:]:
                filename = filenames[i]
                if sub_dir == 'calibration 363' or sub_dir == 'noburst 1998':
                    sub_dir_write = 'val/noburst'
                elif sub_dir == '3 1387':
                    sub_dir_write = 'val/III'
                else:
                    sub_dir_write = 'val/other'
                # 将图片复制到新的文件夹
                shutil.copy(os.path.join(self._path_read, sub_dir, filename),
                            os.path.join(self._path_write, sub_dir_write, filename))
                print('图片{:s}已保存'.format(filename))


if __name__ == '__main__':
    read = r'G:\useful_L\reshape'
    write = r'G:\useful_L\NEW_NET_3.0'
    ImageChoice2(read, write).action()




