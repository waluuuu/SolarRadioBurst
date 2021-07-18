# -*- coding = utf-8 -*-
# @Time : 2021/7/18 16:24
# @Author : 水神与月神
# @File : GetRowDateTimeInfo.py
# @Software : PyCharm


# 由于程序有太多的时间都找不到，所以，进行一下检验，到底是原始数据中没有相关的时间，还是我的程序有问题
import datetime
from ImageSegmentation import read_date
from ImageSegmentation import read_byte

filepath = r'G:\LearmonthData\learmonth原始数据\2005\LM050119.srs'
array = []
with open(filepath, "rb") as f:
    while 1:
        header_data = read_byte(f, 24)  # 返回一个数组，存储前24位数据/如果是cu天文台数据，就是40位的
        if len(header_data) == 0:
            break
        date = read_date(header_data)  # 解析头里面的时间信息，存储在一个数组中
        dt = datetime.datetime(2000 + date[0], date[1], date[2], date[3], date[4], 0)
        print(dt)
        needless = read_byte(f, 802)
