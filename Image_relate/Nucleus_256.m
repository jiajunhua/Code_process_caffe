clear,clc
input='Cell_four_classes_A';
output='cell_256';
dirlist=dir(input);
for dir_num=1:length(dirlist)
    image_path=[input,'\',dirlist(dir_num).name];
    out_path=[output,'\',dirlist(dir_num).name];
    if(~exist(out_path))
        mkdir(out_path)
    end
    imagelist=dir([image_path,'\*.BMP']);
    for image_num=1:length(imagelist)
        image_name=[image_path,'\',imagelist(image_num).name];
        imshow(image_name);
        I =imread(image_name);
        imshow(I);
        [m,n,c]=size(I);
        if(m<256 && n<256)
            out=uint8(zeros(256,256,3));
            out(ceil(128-m/2):ceil(128+m/2)-1,ceil(128-n/2):ceil(128+n/2)-1,:)=I;
        else
            out=imresize(I,[256,256]);
        end       
        outimage=[output,image_name(length(input)+1:end)];
        imwrite(out,outimage)
    end
    
end





