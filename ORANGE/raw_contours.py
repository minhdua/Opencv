import cv2
import numpy as np

def nothing(x):
	pass

def changeThresh(x):
	ret,thresh = cv2.threshold(gray,x,255,cv2.THRESH_BINARY)
	cv2.imshow('Thresh',thresh)

def changeFilter2D(x):
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-x,kernel)
	cv2.imshow('Filter2D',dst)
def changeBlur():
	blur = cv2.blur(img,(5,5))
	cv2.imshow('Blur',blur)
def changeGaussianBlur(x):
	blur = cv2.GaussianBlur(img,(5,5),x)
	cv2.imshow('Gaussian',blur)
def changeMedianBlur(x):
	median = cv2.medianBlur(img,x)
	cv2.imshow('Median',Median)
def changeBilateral():
	x,y,z = 9,95,95
	cv2.namedWindow("Bilateral")
	cv2.createTrackbar("x","Thresh",x,255,nothing)
	cv2.createTrackbar("y","Thresh",y,255,nothing)
	cv2.createTrackbar("z","Thresh",z,255,nothing)
	while True:
		blur = cv2.bilateralFilter(img,x,y,z)
		cv2.imshow('Bilateral',blur)
		k = cv2.waitKey(0)
		if k == 27:
			break

img = cv2.imread('orange.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
def Main():
	x =1
	cv2.namedWindow('Thresh')
	changeBilateral()
	#cv2.createTrackbar("Threshold","Thresh",x,255,changeBilateral)
	# read a image from computer
	# blur image
	# filter color 
	# convert to grayscale
	# covert to binary image
	# b
	changeBlur()
	cv2.imshow('gray',gray)
	cv2.imshow('Contours Orange',img)
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ =='__main__':
	Main()
