# -*- coding = utf-8 -*-
# @Time : 2021/6/18 17:26
# @Author : 水神与月神
# @File : LocalWeb.py
# @Software : PyCharm
import sys

import cv2 as cv
from PyQt5.QtWidgets import QApplication
from keras import backend as K
from ListMerge import list_merge
from TestModel import TestModel
from Normal import Normal
from SlidingWindow import SlidingWindow
from image_show import ImageShow


class LocalWeb:
    """
    设计思路：
    本地实验某个模型应用于大张图片的效果
    需要：
    1. 引入SlidingWindow，循环产生需要的图片
    2. 引入ImageProcess，对图片进行预处理，通道归一化、归一化、变成array
    3. 引入TestModel，判断图片是否属于二型爆
    4. 之后可能会用到： 可以同时引入多个模型

    """

    def __init__(self, image_path, model_path, length, size):
        self._model_path = model_path
        self._image_path = image_path
        self._length = length
        self._size = size

    def process(self):
        positive = []
        images = SlidingWindow(self._image_path, self._length)
        count = 0
        for image_info in images.out():
            image = image_info[0]
            processed = Normal(image, self._size).image_in("Equalization")
            result = TestModel(self._model_path).predict(processed)
            print(result)
            count += 1
            print(count)
            if result < 0.5:
                positive.append([image_info[1], image_info[2]])
            K.clear_session()
        self._show(list_merge(positive))
        return len(list_merge(positive))

    def _show(self, location):
        image = cv.imread(self._image_path, cv.IMREAD_UNCHANGED)
        image = cv.equalizeHist(image)
        image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)
        for i in location:
            cv.rectangle(image, (i[0], 50), (i[1], 750), (255, 0, 0))

        cv.imwrite('image.jpg', image)

        # cv.namedWindow("test", cv.WINDOW_NORMAL)
        # cv.imshow("test", image)
        # cv.waitKey()
        # cv.destroyWindow("test")
