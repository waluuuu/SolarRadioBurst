# -*- coding = utf-8 -*-
# @Time : 2021/6/10 11:32
# @Author : 水神与月神
# @File : ListMerge.py
# @Software : PyCharm
# 列表合并，看演示的效果

def list_merge(ls):
    out = []
    length = len(ls)
    for i in range(length):
        if i == 0:
            out.append(ls[i])
        else:
            if ls[i][0] < out[-1][-1]:
                out[-1][-1] = ls[i][-1]
            else:
                out.append(ls[i])
    return out


if __name__ == '__main__':
    test = [[1, 3], [2, 4], [5, 7], [6, 8], [8, 9]]
    out = list_merge(test)
    print(out)
