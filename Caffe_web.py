#!flask/bin/python
#-*- coding: UTF-8 -*- 
from flask import Flask, jsonify
from flask import request
import matplotlib.pyplot as plt
import cv2
import sys
import numpy as np
import urllib
import caffe
import json
import time
from tempfile import TemporaryFile
import os

app = Flask(__name__)

def url_to_image(url):
	resp = urllib.urlopen(url)
	imageData = bytearray(resp.read())
	#fd, filename = tempfile.mkstemp()
	#print filename
	#f = open(filename, 'wb')
	#f.write(imageData)
	#f.close()
	image = np.asarray(imageData, dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image, imageData
	
cascPath = 'E:\\ImageTool\\haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


#plt.rcParams['figure.figsize'] = (10, 10)
#plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'
# load the mean image

mean_filename='E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\cnn_age_gender_data\\mean.binaryproto'
#mean_filename='.\\cnn_age_gender_data\\mean.binaryproto'
proto_data = open(mean_filename, "rb").read()
a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
mean  = caffe.io.blobproto_to_array(a)[0]
# load the age network
age_net_pretrained='E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\cnn_age_gender_data\\age_net.caffemodel'
age_net_model_file='E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\cnn_age_gender_data\\deploy_age.prototxt'
age_net = caffe.Classifier(age_net_model_file, age_net_pretrained,
                       mean=mean,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(227, 227))

# load the gender network
gender_net_pretrained='E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\cnn_age_gender_data\\gender_net.caffemodel'
gender_net_model_file='E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\cnn_age_gender_data\\deploy_gender.prototxt'
gender_net = caffe.Classifier(gender_net_model_file, gender_net_pretrained,
                       mean=mean,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(227, 227))



mean_file = 'E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\caffe-oxford102-master\\AlexNet\\imagenet_mean.binaryproto'
proto_data = open(mean_file, "rb").read()
a = caffe.io.caffe_pb2.BlobProto.FromString(proto_data)
mean_flower  = caffe.io.blobproto_to_array(a)[0]

flower_net_model_file = 'E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\caffe-oxford102-master\\AlexNet\\deploy.prototxt'
flower_net_pretrained = 'E:\\ImageTool\\03_Code\\AgeGenderDeepLearning\\caffe-oxford102-master\\AlexNet\\oxford102.caffemodel'

flower_net = caffe.Classifier(flower_net_model_file, flower_net_pretrained,
                       mean=mean_flower,
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(227, 227))
   

# age
age_list=['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
gender_list=('man','woman')

# flower
names = ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells', 'sweet pea', 'english marigold', 'tiger lily', 'moon orchid', 'bird of paradise', 'monkshood', 'globe thistle', 'snapdragon', "colt's foot", 'king protea', 'spear thistle', 'yellow iris', 'globe-flower', 'purple coneflower', 'peruvian lily', 'balloon flower', 'giant white arum lily', 'fire lily', 'pincushion flower', 'fritillary', 'red ginger', 'grape hyacinth', 'corn poppy', 'prince of wales feathers', 'stemless gentian', 'artichoke', 'sweet william', 'carnation', 'garden phlox', 'love in the mist', 'mexican aster', 'alpine sea holly', 'ruby-lipped cattleya', 'cape flower', 'great masterwort', 'siam tulip', 'lenten rose', 'barbeton daisy', 'daffodil', 'sword lily', 'poinsettia', 'bolero deep blue', 'wallflower', 'marigold', 'buttercup', 'oxeye daisy', 'common dandelion', 'petunia', 'wild pansy', 'primula', 'sunflower', 'pelargonium', 'bishop of llandaff', 'gaura', 'geranium', 'orange dahlia', 'pink-yellow dahlia?', 'cautleya spicata', 'japanese anemone', 'black-eyed susan', 'silverbush', 'californian poppy', 'osteospermum', 'spring crocus', 'bearded iris', 'windflower', 'tree poppy', 'gazania', 'azalea', 'water lily', 'rose', 'thorn apple', 'morning glory', 'passion flower', 'lotus', 'toad lily', 'anthurium', 'frangipani', 'clematis', 'hibiscus', 'columbine', 'desert-rose', 'tree mallow', 'magnolia', 'cyclamen ', 'watercress', 'canna lily', 'hippeastrum ', 'bee balm', 'ball moss', 'foxglove', 'bougainvillea', 'camellia', 'mallow', 'mexican petunia', 'bromelia', 'blanket flower', 'trumpet creeper', 'blackberry lily']
namesChs = ["粉红樱草花","硬叶兜兰","风铃草","甜豌豆","英国万寿菊","老虎百合","月亮兰花","天堂之鸟","附子","球蓟","鲷鱼","猫头鹰","帝王花","矛蓟","黄鸢", "全球花","紫锥花","秘鲁百合","桔梗","巨大的白色百合", "火百合","枕形花","贝母","红姜","葡萄风信子","虞美人","威尔斯羽毛王子","矮龙胆" ,"朝鲜蓟","甜蜜的威尼康","康乃馨","花园福禄考","雾中的爱","墨西哥的阿斯特","高山海冬","红宝石牛","披风花","伟大的草原","豌豆郁金香","洋葱玫瑰","雏菊","水仙花","剑百合","一品红","波莱罗深蓝", "壁花","万寿菊","毛茛","牛眼雏菊","普通蒲公英","矮牵牛","野生三色堇","普罗布","向日葵","天竺葵","兰达夫主教","古拉","天竺葵","橙色大丽花","大丽花", "距药姜草","日本银莲花","黑眼睛的苏珊","银色树丛","加州罂粟","南非万寿菊","春番红","有髯鸢尾","白头翁","树罂粟", "菊","杜鹃","睡莲","玫瑰","曼陀罗","牵牛花","激情","莲花","蟾蜍百合","安祖花", "鸡蛋花","铁线莲","芙蓉","鸽","沙漠玫瑰","花葵","玉兰","仙客来","豆瓣","美人蕉","朱顶红","蜜蜂花","青苔球","毛地黄","三角梅","茶花","葵","墨西哥矮牵牛","凤梨","花铺盖", "凌霄","黑莓百合"]


# net = caffe.Net(net_file,
                # caffe_model,
                # caffe.TEST)



# print(net.blobs['data'].data.shape)
# transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
# transformer.set_transpose('data', (2, 0, 1))

# transformer.set_mean('data', a)
# transformer.set_raw_scale('data', 255.0)
# transformer.set_channel_swap('data', (2, 1, 0))

@app.route('/detect')
def detect():
	print 'begin:' + time.ctime()
	url = request.args.get('url')
	print url
	image, imageData = url_to_image(url)
	print 'download:' + time.ctime()
#image = caffe.io.load_image(imagePath)
	with TemporaryFile() as tmpfile:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		print 'face begin:' + time.ctime()
		faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
		print 'face end:' + time.ctime()
		tmpfile.write(imageData)
		tmpfile.seek(0)
		imageFile = tmpfile
		if len(faces) == 1:
			print 'load_image begin:' + time.ctime()
			image = caffe.io.load_image(imageFile)
			print 'load_image end:' + time.ctime()
			
			print 'predict begin:' + time.ctime()
			prediction = age_net.predict([image], oversample=False)
			print 'predict end:' + time.ctime()
			
			age = age_list[prediction[0].argmax()]
			print age
			print 'gender begin:' + time.ctime()
			prediction = gender_net.predict([image], oversample=False)
			print 'gender end:' + time.ctime()
			#del  image
			
			print prediction[0].argmax()
			
			print prediction
			
			gender = gender_list[prediction[0].argmax()]
			print gender
			print time.ctime()
			return json.dumps({'type': 'face', 'age' : age, 'gender' : gender})
		else:
			image = caffe.io.load_image(imageFile)
			prediction = flower_net.predict([image], oversample=False)
			
			flower = names[prediction[0].argmax()]
			
			print flower
			#print np.argmax(prob)
			index = np.argmax(prediction)
			print index, prediction[index] 
			print time.ctime()
			if prediction[index] > 0.3:
				return json.dumps({'type': 'flower', 'name' : namesChs[index]})
			else:
				return json.dumps({'type': 'none'})
	#finally:
	#	os.remove(imageFile)

if __name__ == '__main__':
    app.run(debug=True)