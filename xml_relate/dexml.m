clc;clear;
li=ls('*.xml');
for j=1:size(li,1)
    xmlfile=xml_read(li(j,:));
    filename=xmlfile.filename;
    width=xmlfile.size.width;
    heigth=xmlfile.size.height;
    object=xmlfile.object;
    for i=1:size(object,1)
        xmin=object(i).bndbox.xmin;
        ymin=object(i).bndbox.ymin;
        xmax=object(i).bndbox.xmax;
        ymax=object(i).bndbox.ymax;
        if xmin<0
           xmin=0;
       end
    if xmin>=width
        xmin=width;
    end
    if ymin<0
        ymin=0;
    end
    if ymin>=heigth
        ymin=heigth;
    end
    if xmax <0
        xmax=0;
    end
    if xmax>=width
        xmax=width;
    end
    if ymax<0
        ymax=0;
    end
    if ymax>=heigth
        ymax=heigth;
    end
    name=object(i).name;
    if ~isdir(name)
        mkdir(name);
    end
    img=imread(filename);
    imagS=img(ymin:ymax,xmin:xmax);
    imwrite(imagS,['./',name,'/',name,'_',num2str(size(ls(name),1)-1),'.jpg']);
    end
end
clc;clear;

