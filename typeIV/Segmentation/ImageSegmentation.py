# -*- coding = utf-8 -*-
# @Time : 2021/7/18 15:20
# @Author : 水神与月神
# @File : ImageSegmentation.py
# @Software : PyCharm


import datetime
import numpy as np
import cv2 as cv
import openpyxl
import os

count1 = 0
count2 = 0


# 24 802
# 40 501*4


# %%
def read_log(path):
    wb = openpyxl.load_workbook(path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    sheet1 = sheets[0]
    rows = sheet1.rows
    data = []
    count = 0
    for row in rows:
        row_value = [col.value for col in row]
        data.append([row_value[0], row_value[1]])
        count += 1
    print("读取日志的次数", count)
    return data


# %%

def read_byte(bytestream, num):
    """
   :param bytestream: 一个打开的文件
   :param num: 读取字节的数目
   :return: 返回一个数组
   """
    dt = np.dtype(np.uint8)  # 读取字节
    return np.frombuffer(bytestream.read(num), dtype=dt)


# %%

def read_date(head_data):
    """
    当前数据所对应的时间
    :return:返回一个包含时间信息的数组
    """
    time_data = []
    try:
        for i in range(6):
            time_data.append(head_data[i])
        return time_data
    except TypeError:
        print("没有找到数据头")


# %%
def read(filepath, split_time):
    """
    读取数据
    :return:
    """
    array = []
    with open(filepath, "rb") as f:
        while True:
            header_data = read_byte(f, 40)  # 返回一个数组，存储前24位数据/如果是cu天文台数据，就是40位的
            if len(header_data) == 0:
                return array
            date = read_date(header_data)  # 解析头里面的时间信息，存储在一个数组中
            try:
                dt = datetime.datetime(2000 + date[0], date[1], date[2], date[3], date[4], 0)
            except ValueError:
                needless = read_byte(f, 2004)
                print('原始数据中时间标注错误')
                continue
            # 开始条件
            if dt >= split_time[0]:
                while True:
                    needed = read_byte(f, 2004)
                    needed = needed[::-1]
                    array.append(needed)

                    header_data = read_byte(f, 40)  # 返回一个数组，存储前24位数据
                    if len(header_data) == 0:
                        return array
                    date = read_date(header_data)  # 解析头里面的时间信息，存储在一个数组中
                    try:
                        dt2 = datetime.datetime(2000 + date[0], date[1], date[2], date[3], date[4], 0)
                    except ValueError:
                        continue
                    # 结束条件
                    if dt2 >= split_time[1]:
                        return array
            else:
                needless = read_byte(f, 2004)


# %%

def write_image(array, date, save_path):
    global count1
    global count2
    if not array:
        pass
    else:
        # folder = os.path.join(save_path, str(hours))
        folder = save_path
        name_save = "SPEC{:4d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}.jpg"
        if not os.path.exists(folder):
            os.makedirs(folder)
        try:
            array_1d = np.concatenate(array, axis=0)  # 将数组拼接成一整个
            dt = np.dtype(np.uint8)
            array_1d = np.array(array_1d, dtype=dt)
            array_nd = array_1d.reshape(-1, 2004)
            array_nd = np.transpose(array_nd).astype(np.uint8)  # 转置

            image_save_path = os.path.join(folder, name_save.format(date[0].year, date[0].month, date[0].day,
                                                                    date[0].hour, date[0].minute))
            cv.imwrite(image_save_path, array_nd)
            count1 += 1
        except TypeError:
            count2 += 1
            print("没有需要的值")
            print(date)


# %%

if __name__ == '__main__':
    path_read = r"G:\CulgooraData\culgoora原始数据\{:0>2d}"
    path_save = r"G:\CulgooraData\III"
    path_log = r"G:\CulgooraData\log\n2000.xlsx"
    file_name_format = "SPEC{:0>2d}{:0>2d}{:0>2d}"
    # LM{:0>2d}{:0>2d}{:0>2d}.srs
    data = read_log(path_log)
    print(len(data))
    count3 = 0
    count4 = 0
    for one_date in data:
        start_year = one_date[0].year
        start_month = one_date[0].month
        start_day = one_date[0].day
        start_hour = one_date[0].hour

        if start_hour > 20:
            one_date[0] = one_date[0] + datetime.timedelta(hours=24)
            start_month = one_date[0].month
            start_day = one_date[0].day
            file_name = os.path.join(path_read.format(start_year%100),
                                     file_name_format.format(start_year % 100, start_month, start_day))
            one_date[0] = one_date[0] - datetime.timedelta(hours=24)

        else:
            file_name = os.path.join(path_read.format(start_year%100),
                                     file_name_format.format(start_year % 100, start_month, start_day))
        try:
            row_array = read(file_name, one_date)
            write_image(row_array, one_date, path_save)
            count3 += 1
        except FileNotFoundError:
            print(one_date)
            count4 += 1

    print("保存的次数为{:d}\n没有找到数据的次数为{:d}".format(count1, count2))
    print(count3, count4)


