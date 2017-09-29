annotation = xml_read('10_4.xml');
I = imread('10_4.jpg');

object = annotation.object
[object_length, object_lengthtemp] = size(object)
for cnt = 1:object_length
    if strcmp(object(cnt).name,'squamous-hsil')
            bndbox = object(cnt).bndbox;
            x_min_i = bndbox.xmin;
            y_min_i = bndbox.ymin;
            x_max_i = bndbox.xmax;
            y_max_i = bndbox.ymax;
            
            x_min = x_min_i;
            x_max = x_max_i;
            y_min = y_min_i;
            y_max = y_max_i;
            
            
            lineWidth = 3;    
            
            
            I([y_min-lineWidth:y_min+lineWidth, y_max-lineWidth:y_max+lineWidth], x_min:x_max, :) = 0;
            I(y_min:y_max, [x_min-lineWidth:x_min+lineWidth, x_max-lineWidth:x_max+lineWidth], :) = 0;
            I([y_min-lineWidth:y_min+lineWidth, y_max-lineWidth:y_max+lineWidth], x_min:x_max, 2) = 255;
            I(y_min:y_max, [x_min-lineWidth:x_min+lineWidth, x_max-lineWidth:x_max+lineWidth], 2) = 255;            
            
    end
    
    
end
cnt
imshow(I)
size(I)
imwrite(I,'1.jpg')