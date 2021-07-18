# -*- coding = utf-8 -*-
# @Time : 2021/7/17 19:42
# @Author : 水神与月神
# @File : GetSegmentationTime.py
# @Software : PyCharm

"""
关于这个程序的说明，
持续时长超过五小时的IV型爆，直接用别的程序复制的指定路径

其余的需要划定分割时间

"""

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
        self.threshold_II = 1200
        # 0-30min : 1h    0
        # 30min-1h : 2h   1
        # 1h-2h : 4h      2 3
        # 2h - 5h : 8h    4 5 6 7 8 9
        # 5h以上 ： 整张图片 10
        self.seg_time_II = {0: 1, 1: 2, 2: 4, 3: 4, 4: 8, 5: 8, 6: 8, 7: 8, 8: 8, 9: 8}

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

            temp_use = []
            if int((row_value[1] - row_value[0]).seconds / 3600 // 0.5) >= 10:
                continue
            d1, d2 = mySplit(row_value[0], row_value[1],
                             self.seg_time_II[int((row_value[1] - row_value[0]).seconds / 3600 // 0.5)])

            temp_use.append(d1)  # 开始时间
            temp_use.append(d2)  # 结束时间
            temp_use.append((d2 - d1).seconds//3600)  # 持续时间
            temp_use.append(row_value[3])  # 最低频率
            temp_use.append(row_value[4])  # 最高频率
            temp_use.append(row_value[5])  # 频率跨度
            temp_use.append(row_value[6])  # 大类
            temp_use.append(row_value[7])  # filename
            temp_use.append(row_value[8])  # filepath
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
    read_path = r"C:\Users\dell\Desktop\new.xlsx"
    save_path = r"C:\Users\dell\Desktop\IVSegmentationTime.xlsx"
    GetSegmentationTime(read_path, save_path).newDate()
