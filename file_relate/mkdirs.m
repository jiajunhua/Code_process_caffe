clc;
clear;

path='I:\Pap_data_0824';
newPath = 'I:\0824_TMAP_img';
fileList=dir(path);

for i=3:length(fileList)
    names = fullfile(newPath,fileList(i).name); 
    if(~isdir(names(1:length(names)-5)))
        mkdir(names(1:length(names)-5));
    end
end