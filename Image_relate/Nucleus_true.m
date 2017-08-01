clear,clc
input='New database pictures';
output='nucleus_only_128';
dirlist=dir(input);
for dir_num=3:length(dirlist)
    image_path=[input,'\',dirlist(dir_num).name];
    out_path=[output,'\',dirlist(dir_num).name];
    if(~exist(out_path))
        mkdir(out_path)
    end
    imagelist=dir([image_path,'\*d.bmp']);
    for image_num=1:length(imagelist)
        image_name=[image_path,'\',imagelist(image_num).name];
        
        [I,map]=imread(image_name);
        I=ind2rgb(I,map);
        b=I(:,:,3);
        bw=im2bw(b,0.9);
        image_name=[image_name(1:end-6),'.bmp'];
        I=imread(image_name);
        nucleus=I.*uint8(bw);
        bw=im2bw(nucleus,0.01);
        
        l=bwlabel(bw,8);            
        stats = regionprops(l,'Area');   
        area = cat(1,stats.Area);
        index = find(area == max(area));        
        l = ismember(l,index);          
        
        status=regionprops(l,'BoundingBox');
        box=status(1).BoundingBox;
        nucleus=nucleus(:,ceil(box(1)):floor(box(1)+box(3)),:,:);
        nucleus=nucleus(ceil(box(2)):floor(box(2)+box(4)),:,:);
        [m,n,c]=size(nucleus);
        if(m<128 & n<128)
            out=uint8(zeros(128,128,3));
            out(ceil(64-m/2):ceil(64+m/2)-1,ceil(64-n/2):ceil(64+n/2)-1,:)=nucleus;
        else
            out=imresize(nucleus,[128,128]);
        end
        
        
        outimage=[output,image_name(length(input)+1:end)];
        imwrite(out,outimage)
    end
    
end


