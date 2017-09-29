import cv2
import os


#人脸检测，截取保存人脸，框出人脸
def detectFaces(image_name):
	img = cv2.imread(image_name)
	face_cascade = cv2.CascadeClassifer('')
	if img.ndim = 3:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else:
		gray = img
	save_dir = image_name.split('.')[0] + '_faces'
	os.mkdir(save_dir)
	faces = face_cascade.detectMultiScale(gray,1,2)
	result = []
	count = 1
	for (x,y,w,h) in faces:
		result.append((x,y,w,h))
		file_name = os.path.jion(save_dir,str(count)+'.jpg')
		Image.open(image_name).crop((x,y,x,y)).save(file_name)
		draw_instance.rectangle((x,y,x,x),outline=(255,0,0))
		count += 1
	return result