# -*- coding = utf-8 -*-
# @Time : 2021/8/4 23:07
# @Author : kinghe
# @File : main.py
# @Software : PyCharm
import os
import sys
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from image_show import ImageShow
from solar_spectrum import Ui_MainWindow
from PyQt5 import QtWidgets
from LocalWeb import LocalWeb


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        self._my_filename = ''
        self.burst_number = 0
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.image_show = ImageShow()
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton.clicked.connect(self.onStart)
        self.pushButton.clicked.connect(self.image_classification)
        self.pushButton_3.clicked.connect(self.image_show.show)
        self.timer = QBasicTimer()
        self.step = 0

    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
            self.label.setText('太阳射电爆发图片检测中')

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.step = 0
            my_str = "太阳射电爆发图片检测已完成 共%d个爆发区域" % self.burst_number
            QMessageBox.information(self, '提示', my_str)
            self.label.setText('图片检测已完成')
            return
        self.step = self.step + 1
        self.progressBar.setValue(self.step)

    def open_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "图片文件(*.png);;(*.jpeg);;(*.jpg)")
        ui.lineEdit.setText(fileName)
        # print(fileName)
        # print(fileType)
        self._my_filename = fileName
        self.label.setText('爆发图片准备中')
        self.progressBar.setValue(self.step)

    def image_classification(self):

        image_path = self._my_filename
        model_path = r'F:\SolarRadioBurst\测试通道归一化\3\二分类\实验1.1_best.h5'
        length = 200
        size = (400, 100)
        local_web = LocalWeb(image_path, model_path, length, size)
        self.burst_number = local_web.process()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainForm()
    ui.show()
    sys.exit(app.exec_())
