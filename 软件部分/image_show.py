# -*- coding = utf-8 -*-
# @Time : 2021/8/14 0:13
# @Author : kinghe
# @File : image_show.py
# @Software : PyCharm
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QScrollArea, QScrollBar, \
    QHBoxLayout, QVBoxLayout, QApplication


class ImageShow(QWidget):
    def __init__(self):
        super(ImageShow, self).__init__()
        self.label = QLabel(self)  # 1
        self.label.setPixmap(QPixmap('image.jpg'))
        self.label.setScaledContents(True)

        self.scroll_area = QScrollArea(self)  # 2
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollbar = QScrollBar(Qt.Horizontal, self)  # 3
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

        self.bigger_btn = QPushButton('放大', self)  # 4
        self.smaller_btn = QPushButton('缩小', self)

        self.bigger_btn.clicked.connect(self.bigger_func)  # 5
        self.smaller_btn.clicked.connect(self.smaller_func)
        self.scrollbar.valueChanged.connect(self.sync_func)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.bigger_btn)
        self.h_layout.addWidget(self.smaller_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        self.v_layout.addWidget(self.scrollbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
        self.setWindowTitle('solar_spectrum')

    def bigger_func(self):
        self.label.resize(self.label.width() * 1.2, self.label.height() * 1.2)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

    def smaller_func(self):
        self.label.resize(self.label.width() * 0.8, self.label.height() * 0.8)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

    def sync_func(self):
        self.scroll_area.horizontalScrollBar().setValue(self.scrollbar.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ImageShow()
    demo.show()
    sys.exit(app.exec_())
