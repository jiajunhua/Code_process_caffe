# !/usr/bin/env python
# encoding: utf-8

import os
import glob
from PIL import Image


outDir = os.path.abspath('H:\\xml\\22')
# path2Image = 'F:\\Pap_cell\\Import_data\\Dataset_DL\\test'
# Images = os.listdir(path2Image)

imageDir1 = os.path.abspath('I:\\0824_TMAP_img\\P173669')


image1 = []
imgname1 = []

imageList1 = glob.glob(os.path.join(imageDir1, '*.jpg'))

for item in imageList1:
    image1.append(os.path.basename(item))

for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)


imageDir2 = os.path.abspath('H:\\xml\\2')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.xml'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)


for item1 in imgname1:
    for item2 in imgname2:
        if item1 == item2:
            dir = imageList1[imgname1.index(item1)]
            img = Image.open(dir)
            name = os.path.basename(dir)
            img.save(os.path.join(outDir, name))
