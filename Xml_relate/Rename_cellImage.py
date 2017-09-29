# -*- coding: utf-8 -*-
import os
import sys
import glob
from scipy import misc
from PIL import Image
from os.path import join, getsize

dir_list = os.listdir("I:\\0824__img\\")

for dir_ in dir_list[13:-1]:

    image_files = glob.glob("I:\\0824__img\\" + dir_ + "\\*.jpg")

    dir_files = "I:\\0824__img\\" + dir_

    print dir_files

    if len(image_files) == 0:
        continue
    name = dir_[3:7]
    prefix = 'P' + name + '_'

    Images = os.listdir(dir_files)

    for Image in Images:

        filename, file_extension = os.path.splitext(Image)
        # print file_extension
        if file_extension == '.jpg':
            # print Image
            # print Image
            OldName = Image
            OldDir = os.path.join(dir_files, OldName)
            NewName = prefix + OldName
            NewDir = os.path.join(dir_files, NewName)
            os.rename(OldDir, NewDir)