# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image


outDir = os.path.abspath('F:\\Pap_cell\\Import_data\\Dataset_DL\\out')
# path2Image = 'F:\\Pap_cell\\Import_data\\Dataset_DL\\test'
# Images = os.listdir(path2Image)

imageDir1 = os.path.abspath('F:\\Pap_cell\\Import_data\\Dataset_DL\\VOC2007-0805\\JPEGImages')


image1 = []
imgname1 = []

imageList1 = glob.glob(os.path.join(imageDir1, '*.jpg'))

for item in imageList1:
    image1.append(os.path.basename(item))

for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)
print imgname1

"""

# xml解析
imageDir2 = os.path.abspath('I:\\D_to_I\\0602_02')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.xml'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)
"""
# 切割txt
data = []
data_num = []
f = open('F:\\Pap_cell\\Import_data\\Dataset_DL\\VOC2007-0805\\ImageSets\\Maintest.txt')
lines = f.readlines()
for line in lines:
    # print line
    data.append(line)
for item in data:
    (temp1, temp2) = item.split('\n')
    data_num.append(temp1)

for item1 in imgname1:
    for item2 in data_num:
        if item1 == item2:
            dir = imageList1[imgname1.index(item1)]
            print dir
            img = Image.open(dir)
            name = os.path.basename(dir)
            img.save(os.path.join(outDir, name))
