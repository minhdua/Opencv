import cv2
import numpy as np

def changeImage(x):
	print(x)
	ret,thresh = cv2.threshold(gray,x,255,cv2.THRESH_BINARY)
	cv2.imshow('Thresh',thresh)

x = 127
img = cv2.imread('orange.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.namedWindow('Thresh')
cv2.createTrackbar("Threshold","Thresh",x,255,changeImage)
# read a image from computer
# blur image
# filter color 
# convert to grayscale
# covert to binary image
# b
cv2.imshow('gray',gray)
cv2.imshow('Contours Orange',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

