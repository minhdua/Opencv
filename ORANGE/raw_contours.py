import cv2
import numpy as np

def GaussianBlur(img):
	blur = cv2.GaussianBlur(img,(5,5),-1)
	return blur

def changeMask():
	x0,x1,y0,y1,z0,z1= 6,31,171,255,171,255
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	low = np.array([x0,y0,z0])
	upper = np.array([x1,y1,z1])
	mask = cv2.inRange(hsv,low,upper)
	result = cv2.bitwise_and(img,img,mask=mask)
	return result

def drawContours():
	img2 = changeMask()
	gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray2,10,255,cv2.THRESH_BINARY)
	blur = GaussianBlur(thresh)
	contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow('gray2',gray2)
	cv2.imshow('thresh',thresh)
	cv2.drawContours(img, contours, 0, (0,255,0), 3)

img = cv2.imread('orange.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

def Main():
	drawContours()
	cv2.imshow('Contours Orange',img)
	while True:
		k = cv2.waitKey(1)
		if k ==27 :
			break
		
	cv2.destroyAllWindows()

if __name__ =='__main__':
	Main()
