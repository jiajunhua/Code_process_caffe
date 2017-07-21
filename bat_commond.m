clc;
clear;

path='I:\0720_TMAP_img';
newPath = 'I:\0720_TMAP_img_cell';
fileList=dir(path);
dirList = dir(newPath);

fid = fopen('C.bat','wt');

for i=1:8
    fprintf(fid,'%s\t','C:\Users\way\Desktop\ParseTMap_1024\ParseTMap.exe');
    fprintf(fid,'%s\t',fullfile(path,fileList(i+2).name));
    fprintf(fid,'%s\n',fullfile(newPath,fileList(i+2).name(1:length(fileList(i+2).name)-5)));
end

fclose(fid);

