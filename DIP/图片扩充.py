# -*- coding = utf-8 -*-
# @Time : 2021/7/29 8:40
# @Author : 水神与月神
# @File : 图片扩充.py
# @Software : PyCharm

# 某类图片数量较少时，进行扩充
# 直接使用《python深度学习》这本书上的代码，最好不要加上平移，不然可以明显看出是扩充过的
import os
import cv2 as cv
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

path_read = r'G:\useful_L\reshape\noburst 1998'
path_write = r'G:\useful_L\reshape\newnoburst'

datagen = ImageDataGenerator(
    width_shift_range=0.2,
    height_shift_range=0.05,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

for fname in os.listdir(path_read):
    img = image.load_img(os.path.join(path_read, fname), target_size=None)
    x = image.img_to_array(img)
    x = x.reshape((1,) + x.shape)

    for batch in datagen.flow(x, batch_size=1):
        image_array = batch[0]
        file_name = 'extend_' + fname
        cv.imwrite(os.path.join(path_write, file_name), image_array)
        print('扩充图像{:s}保存完毕'.format(file_name))
        break
