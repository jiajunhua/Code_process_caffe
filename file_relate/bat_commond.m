clc;
clear;

path='I:\Pap_data_0824';
newPath = 'I:\0824_TMAP_img';
fileList=dir(path);
dirList = dir(newPath);

fid = fopen('PapCell.bat','wt');

for i=1:70
    fprintf(fid,'%s\t','C:\Users\way\Desktop\ideepwise_Papcell\ParseTMap_1024\ParseTMap.exe');
    fprintf(fid,'%s\t',fullfile(path,fileList(i+2).name));
    fprintf(fid,'%s\n',fullfile(newPath,fileList(i+2).name(1:length(fileList(i+2).name)-5)));
end

fclose(fid);

