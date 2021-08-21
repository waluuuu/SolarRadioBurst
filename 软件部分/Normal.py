# -*- coding = utf-8 -*-
# @Time : 2021/6/18 15:14
# @Author : 水神与月神
# @File : ImageProcess.py
# @Software : PyCharm


import numpy as np
import cv2 as cv


class Normal:
    """
    图像处理的类，
    得到需要的图片
    1. 改变大小和归一化
    """

    def __init__(self, image, size=(400, 200)):

        self._image = image
        self._size = size[1], size[0]  # 使用opencv，需要进行前后互换

    def _normalization_x(self):
        # 徐龙老师采用的消除横线噪声的通道归一化方法
        img = self._image.copy()
        # list 没有shape方法
        shape = img.shape
        global_mean = np.mean(img)
        # 防止255溢出，先将数组转换成列表
        img = img.tolist()
        for i in range(shape[0]):
            channel_mean = np.mean(img[i])
            img[i] = img[i] - channel_mean + global_mean
        img = np.array(img, dtype=np.uint8)
        return img

    def _normalization_z(self):
        # 张沛锦采用的消除背景缓变噪声的通道归一化方法
        img = self._image.copy()
        # list 没有shape方法
        shape = img.shape
        # 防止255溢出，先将数组转换成列表
        image = img.tolist()

        for i in range(shape[0]):
            channel_mean = np.mean(image[i])
            image[i] = abs(image[i] - channel_mean)
        image = np.array(image, dtype=np.uint8)
        return image

    def image_in(self, process="NORMAL_X"):
        """
        :param process:
        NORMAL_X : 徐龙老师的通道归一化，默认方法
        NORMAL_Z : 张沛锦前辈的通道归一化
        Equalization : 直方图均衡


        后续会添加别的数字图像处理方法
        这个架构好像不适合添加别的方法了，因为别的方法需要添加参数，放到一个类里面不合适
        :return: 返回一个array
        """
        if process == "NORMAL_X":
            out = self._normalization_x()
        elif process == "Equalization":
            out = self._normalization_z()
            out = cv.cvtColor(out, cv.COLOR_BGR2GRAY)
            out = cv.equalizeHist(out)
            out = cv.cvtColor(out, cv.COLOR_GRAY2RGB)
        else:
            out = self._normalization_x()

        out = cv.resize(out, self._size)
        out = out / 255.0
        temp = [out]
        return np.array(temp)

    def process(self, method="NORMAL_X"):
        if method == "NORMAL_X":
            image = self._normalization_x()
        elif method == "NORMAL_Z":
            image = self._normalization_z()
        else:
            return None
        return image



