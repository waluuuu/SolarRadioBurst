# -*- coding = utf-8 -*-
# @Time : 2021/7/16 20:02
# @Author : 水神与月神
# @File : excel.py
# @Software : PyCharm
# 读取的写入excel文件

import openpyxl


class Excel:
    """
    使用的时候，需要重写_info_filter、_change_header
    """

    def __init__(self, path_read, path_write, info=None, header=None, types=None):
        if info is None:
            info = []
        if header is None:
            header = []

        self._path_read = path_read
        self._path_write = path_write
        self._type = types

        self._info = info
        self._header = header

    def _read(self):
        if not self._info:
            print('到这一步了')
            self._wb_read = openpyxl.load_workbook(self._path_read)
            sheets = self._wb_read.worksheets  # 获取当前所有的sheet
            sheet = sheets[0]
            rows = sheet.rows

            for row in rows:
                row_value = [col.value for col in row]
                self._info_filter(row_value)

            if not self._header:
                self._header = self._info.pop(0)
            else:
                self._info.pop(0)  # 删除开头的数据也即表头

    def _info_filter(self, info):
        pass

    def _write(self):
        if self._type == 'w':
            pass
        else:
            self._read()
        self._wb_write = openpyxl.Workbook()
        ws = self._wb_write.active
        ws.append(self._header)
        print('已经写入header了')
        print(len(self._info))
        for row in self._info:
            ws.append(row)
        print('全部写入')
        self._wb_write.save(self._path_write)
        print('保存成功')

    def write(self):
        self._write()

    def read(self):
        self._read()

    @property
    def info(self):
        return self._info
