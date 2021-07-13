# -*- coding = utf-8 -*-
# @Time : 2021/6/18 17:26
# @Author : 水神与月神
# @File : LocalWeb.py
# @Software : PyCharm

import cv2 as cv
from ListMerge import list_merge
from TestModel import TestModel
from DIP.Normal import Normal
from SlidingWindow.SlidingWindow import SlidingWindow


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
        for image_info in images.out():
            image = image_info[0]
            processed = Normal(image, self._size).image_in("NORMAL_X")
            result = TestModel(self._model_path).predict(processed)
            print(result)
            if result < 0.5:
                positive.append([image_info[1], image_info[2]])
        self._show(list_merge(positive))

    def _show(self, location):
        image = cv.imread(self._image_path)
        for i in location:
            cv.rectangle(image, (i[0], 0), (i[1], 800), (255, 0, 0))

        cv.imshow("test", image)
        cv.waitKey()
        cv.destroyWindow("test")


if __name__ == '__main__':
    image_path = r'G:\LearmonthData\learmonth_pics2\10\LM100102.srs.png'
    model_path = r'F:\SolarRadioBurst\typeIII\typeIII_binary_normalization_100_1.4_50.h5'
    length = 200
    size = (400, 100)
    local_web = LocalWeb(image_path, model_path, length, size)
    local_web.process()


