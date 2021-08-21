# -*- coding = utf-8 -*-
# @Time : 2021/6/18 14:39
# @Author : 水神与月神
# @File : test_model.py
# @Software : PyCharm
# predict模块用来生成模型的检测结果，和真实值比较后，可以得到准确率，进一步得到TPR/FPR

from keras.models import load_model


class TestModel:
    """
    检测一个模型的实际使用准确性
    1. 引入模型
    2. 输入图片，检测效果
    """

    def __init__(self, model_path):
        """
        初始化，引入模型
        :param model_path:
        """
        self._model = load_model(model_path)

    def predict(self, image):
        return self._model.predict(image)

    def predict_classes(self, image):
        return self._model.predict_classes(image)
