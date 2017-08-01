# -*- coding: utf-8 -*-
import os
path2Image = 'F:\\Pap_cell\\Import_data\\Dataset_DL\\04'
Images = os.listdir(path2Image) 
prefix = '04_'
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