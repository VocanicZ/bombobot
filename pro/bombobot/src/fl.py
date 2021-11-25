import cv2 as cv

path = 'C:/Users/ampna/Github/work/pro/bombobot/src'

def set_img(name, img):
	cv.imwrite(path+'/img/'+name+'.png', img)

def get_img(name):
	return cv.imread(path+'/img/'+name+'.png')

def get_img_path(name):
	return path+'/img/'+name+'.png'