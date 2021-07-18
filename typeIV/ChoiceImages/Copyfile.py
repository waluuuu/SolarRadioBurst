# -*- coding = utf-8 -*-
# @Time : 2021/7/17 10:52
# @Author : 水神与月神
# @File : Copyfile.py
# @Software : PyCharm

import os
import shutil
import openpyxl
from Classes.Excel import Excel

log_path = r'C:\Users\dell\Desktop\IV.xlsx'


class ReadLog(Excel):
    def _info_filter(self, info):
        self._info.append([info[-2] + '.png', info[-1] + '.png'])

    def _read(self):
        if not self._info:
            print('到这一步了')
            self._wb_read = openpyxl.load_workbook(self._path_read)
            sheets = self._wb_read.worksheets  # 获取当前所有的sheet
            sheet = sheets[4]
            rows = sheet.rows

            for row in rows:
                row_value = [col.value for col in row]
                self._info_filter(row_value)

            if not self._header:
                self._header = self._info.pop(0)
            else:
                self._info.pop(0)  # 删除开头的数据也即表头


excel = ReadLog(log_path, None, types='r')

excel.read()
paths = excel.info
base_path = r'G:\LearmonthData\learmonth_pics'
new_path = r'G:\LearmonthData\IV\5-12h'

for path in paths:
    full_path = os.path.join(base_path, path[-1])
    new_full_path = os.path.join(new_path, path[-2])
    try:
        shutil.copyfile(full_path, new_full_path)
    except FileNotFoundError:
        pass


