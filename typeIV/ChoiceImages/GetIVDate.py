# -*- coding = utf-8 -*-
# @Time : 2021/7/16 19:56
# @Author : 水神与月神
# @File : GetIVDate.py
# @Software : PyCharm
import datetime

from Classes.Excel import Excel


class GetIVDate(Excel):

    def _info_filter(self, info):
        if (info[6] == 'III') or (info[6] == 'II') or (info[6] == 'V'):
            pass
        else:
            try:
                year = info[0].year
                month = info[0].month
                day = info[1].day if int(info[1].hour) < 15 else (info[1] + datetime.timedelta(days=1)).day
                file_name_format = "LM{:0>2d}{:0>2d}{:0>2d}.srs"

                filename = file_name_format.format(year % 10, month, day)
                filepath = str(year) + '\\' + filename
                info.append(filename)
                info.append(filepath)
                self._info.append(info)

            except AttributeError:
                pass


if __name__ == '__main__':
    path_read = r'G:\LearmonthData\日志文件合并\2001-2020合并清洗统计.xlsx'
    path_save = r'G:\LearmonthData\日志文件合并\2001-2020其它类型.xlsx'
    header = ['startTime', 'endTime', 'duration', 'startFre', 'endFre', 'Frequency', 'types', 'filename',
              'filepath']
    IV = GetIVDate(path_read, path_save, header=header)
    IV.write()
