clc;
clear;

path='I:\0720_TMAP_img';
newPath = 'I:\0720_TMAP_img_cell';
fileList=dir(path);

for i=3:length(fileList)
    names = fullfile(newPath,fileList(i).name); 
    if(~isdir(names(1:length(names)-5)))
        mkdir(names(1:length(names)-5));
    end
end