%%  
% The code used to create train.txt in faster-RCNN 
%%  

xmlfilepath='C:\Users\way\Desktop\ideepwise_mxnet\VOC2007_0918\Annotations';  
txtsavepath='C:\Users\way\Desktop\ideepwise_mxnet\VOC2007_0918\ImageSets\Main\';  
trainval_percent=0.8;
train_percent=0.8;
  
  
%%  
xmlfile=dir(xmlfilepath);  
numOfxml=length(xmlfile)-2;
  
  
trainval=sort(randperm(numOfxml,floor(numOfxml*trainval_percent)));  
test=sort(setdiff(1:numOfxml,trainval));  
  
  
trainvalsize=length(trainval);
train=sort(trainval(randperm(trainvalsize,floor(trainvalsize*train_percent))));  
val=sort(setdiff(trainval,train));  
  
  
ftrainval=fopen([txtsavepath 'trainval.txt'],'w');  
ftest=fopen([txtsavepath 'test.txt'],'w');  
ftrain=fopen([txtsavepath 'train.txt'],'w');  
fval=fopen([txtsavepath 'val.txt'],'w');  
  
  
for i=1:numOfxml  
    if ismember(i,trainval)  
        fprintf(ftrainval,'%s\n',xmlfile(i+2).name(1:end-4));  
        if ismember(i,train)  
            fprintf(ftrain,'%s\n',xmlfile(i+2).name(1:end-4));  
        else  
            fprintf(fval,'%s\n',xmlfile(i+2).name(1:end-4));  
        end  
    else  
        fprintf(ftest,'%s\n',xmlfile(i+2).name(1:end-4));  
    end  
end  
fclose(ftrainval);  
fclose(ftrain);  
fclose(fval);  
fclose(ftest); 