# -*- coding = utf-8 -*-
# @Time : 2021/6/18 15:40
# @Author : 水神与月神
# @File : SlidingWindow.py
# @Software : PyCharm


import cv2 as cv
from keras.preprocessing.image import load_img, img_to_array


class SlidingWindow:
    """
    采用自定义滑窗法，生成需要的图片
    从左到右，每次生成length长度的图片，图片之间有half_length的重叠部分
    防止最后有遗漏，从最后面返回一张长length的图片
    """

    def __init__(self, image_path, length):
        self._image = img_to_array(load_img(image_path))
        self._length = length  # 划取长度

    def out(self):
        length = self._image.shape[1]  # 图片的长度
        half_l = self._length // 2  # 划取长度的一半

        times = (length - half_l) // half_l
        for i in range(times):
            out = self._image[:, i * half_l:i * half_l + self._length, :]
            yield out, i * half_l, i * half_l + self._length

        # 返回最后一张图片
        out = self._image[:, -1 - self._length:-1, :]
        yield out, length - self._length, length


###################################################

# path = r"C:\Users\dell\Desktop\LM030122.srs.png"
# image = img_to_array(load_img(path))
# image2 = cv.imread(path)
#
# print(type(image))
# print(type(image2))
# print((image == image2).all())
