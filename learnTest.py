#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import glob
from scipy import misc
from PIL import Image
from os.path import join, getsize


def data_process(image_files):

    for image_file in image_files:

        res = os.path.getsize(image_file)
        if res < 102400:
            os.remove(image_file)
        else:
            print 'nice'


dir_list = os.listdir("I:\\0720_TMAP_img_cell")

for dir_ in dir_list:

    image_files = glob.glob("I:\\0720_TMAP_img_cell\\" + dir_ + "\\*.jpg")

    if len(image_files) == 0:
        continue

    data_process(image_files)



