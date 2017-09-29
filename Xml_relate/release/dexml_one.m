function dexml(infilename)
%简单的读写XML文件?

xmlfile=xml_read(infilename);
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
    img=imread(filename);
    imagS=img(ymin:ymax,xmin:xmax);
    imwrite(imagS,['./',name,'/',num2str(str2num(filename(1:6))*10+i),'.jpg'])
end

