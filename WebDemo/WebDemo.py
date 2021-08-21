# -*- coding = utf-8 -*-
# @Time : 2021/6/13 22:45
# @Author : 水神与月神
# @File : WebDemo.py
# @Software : PyCharm

# 本地执行localWeb的代码，配合php文件一起运行

import os
import cv2 as cv
from time import sleep
import ListMerge
from keras.models import load_model

while True:
    #  设置休眠时间
    sleep(1)
    #  检测文件夹，进行遍历寻找
    path = r'D:\\Apache24\\htdocs\\SolarBurst\\images\\'
    filenames = os.listdir(path)
    if filenames:
        filename = filenames[0]
        model_III = load_model(r'F:\SolarRadioBurst\typeIII\typeIII_binary_normalization_100_1.3_50_2.h5')
        possible = []
        for image, start, end in demo.img_generator(os.path.join(path, filename), 200):
            result = model_III.predict(image)
            print(result)
            if result < 0.5:
                possible.append([start, end])

        out = ListMerge.list_merge(possible)
        print(out)
        print("一共找到{:d}个三型爆".format(len(out)))

        image = cv.imread(os.path.join(path, filename))

        for i in out:
            cv.rectangle(image, (i[0], 0), (i[1], 800), (0, 255, 0))

        cv.imwrite(r'D:\Apache24\htdocs\SolarBurst\images\processed.png', image)

        break