# -*- coding = utf-8 -*-
# @Time : 2021/7/29 10:28
# @Author : 水神与月神
# @File : 训练集2.0.py
# @Software : PyCharm

# 这是一种新的思路，所以用2来开头

from Classes.ImageChoice import ImageChoice

read = r'G:\useful_L\reshape'
write = r'G:\useful_L\NEW_NET_2.0'
IC = ImageChoice(read, write).action()
