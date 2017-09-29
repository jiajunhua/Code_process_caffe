# -*- coding: utf-8 -*-
import os
path2Image = "C:\\Users\\way\\Desktop\\ideepwise_mxnet\\Human_label\\0918\\2343L"
Images = os.listdir(path2Image) 
prefix = '2343_'
for Image in Images:
    filename, file_extension = os.path.splitext(Image)
    # print file_extension
    if file_extension == '.jpg':
        # print Image
    # print Image
        OldName = Image
        OldDir = os.path.join(path2Image,OldName)
        NewName = prefix + OldName
        NewDir = os.path.join(path2Image,NewName)
        os.rename(OldDir, NewDir)