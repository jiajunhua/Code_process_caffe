%% Yawei Li 20170727
% Print the cell infomation

clear all;close all;clc;
fprintf('------------------------begin------------------------------\n')
PATH ='C:\Users\way\Desktop\ideepwise_mxnet\VOC2007_0918\Annotations\';
Files = dir(strcat(PATH,'*.xml'));
lengthFiles = length(Files);
fid = fopen('CellBBoxInformation_0919.txt','w');
fid1 = fopen('CellBBoxInformation_test.txt','w');
%cell_test = 'squamous-asc';
for i = 1:lengthFiles
    annotation = xml_read(strcat(PATH,Files(i).name));
    object = annotation.object;
    [object_length, object_length_temp] = size(object);
    for j = 1:object_length
        name = Files(i).name;
        class = object(j).name;
        class;
        xmin = object(j).bndbox.xmin;
        xmax = object(j).bndbox.xmax;
        ymin = object(j).bndbox.ymin;
        ymax = object(j).bndbox.ymax;
        if ((ymin == ymax)||(xmax == xmin))
            fprintf(fid,'%s\t\t%s\n',name,class);
        elseif xmax == xmin
            fprintf(fid,'%s\t\t%s\n',name,class);
        elseif ((xmin == 0) || (xmax == 0) || (ymin==0)||(ymax==0))
            fprintf(fid1,'%s\t\t%s\n',name,class);
        end
        
    %     fid = fopen('test.txt','w');
        % ¥Ú”°–≈œ¢
        %fprintf(fid,'%s\t\t%s\t\t%d\t%d\t%d  %d\t\n',name,class,xmin,ymin,xmax,ymax);
%         if strcmp(class,cell_test)
%             fprintf(fid,'%s\t\t%s\t\t%d\t%d\t%d  %d\t\n',name,class,xmin,ymin,xmax,ymax);
%         end
            
    %     fclose(fid);
    end
    fprintf(fid,'\n');
    fprintf(fid1,'\n');
end
fclose(fid);
fclose(fid1);
fprintf('-------------------------end-------------------------------\n')