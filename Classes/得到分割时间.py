# -*- coding = utf-8 -*-
# @Time : 2021/8/1 20:01
# @Author : 水神与月神
# @File : CIII.py
# @Software : PyCharm
# 根据日志中爆发的时间，设置切割图片的时间


import openpyxl
import datetime


def mySplit(startTime, endTime, duration):
    """
    duration: 持续时间，用小时表示
    """
    # 两个时间不能相加
    mid_time = startTime + (endTime - startTime) / 2
    d1 = mid_time - datetime.timedelta(hours=duration / 2)
    d2 = d1 + datetime.timedelta(hours=duration)
    return d1, d2


class GetSegmentationTime:
    def __init__(self, path_read, path_save):
        self.read_path = path_read
        self.save_path = path_save

    def getSegmentationTime(self):
        wb = openpyxl.load_workbook(self.read_path)
        sheets = wb.worksheets  # 获取当前所有的sheet
        # 获取第一张sheet
        sheet1 = sheets[0]
        rows = sheet1.rows
        data = []
        # 迭代读取所有的行
        for row in rows:
            # 获得每一行的全部值
            row_value = [col.value for col in row]
            if row_value[5] != 'III':
                continue
            if int((row_value[1] - row_value[0]).seconds / 60) >= 15:
                continue

            temp_use = []
            d1, d2 = mySplit(row_value[0], row_value[1], 1/6)
            temp_use.append(d1)  # 开始时间
            temp_use.append(d2)  # 结束时间
            data.append(temp_use)

        return data

    def saveDate(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        for row in self.getSegmentationTime():
            ws.append(row)
        wb.save(self.save_path)
        print("成功保存！")

    def newDate(self):
        self.saveDate()


if __name__ == "__main__":
    read_path = r"G:\CulgooraData\log\1994-2015合并.xlsx"
    save_path = r"G:\CulgooraData\log\newIII.xlsx"
    GetSegmentationTime(read_path, save_path).newDate()


