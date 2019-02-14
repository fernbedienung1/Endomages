#!/usr/bin/env	python3

import cv2
import numpy as np

# img = cv2.imread('murcielago.jpg')
cap = cv2.VideoCapture(1)


while True :
	_, frame = cap.read()	# python _ --> not used
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# use unique color		in this case I am looking for my Green HAIR
	lower_grn = np.array([50, 40, 0]) 		#they are already HSV
	upper_grn = np.array([100, 255, 255])

	mask = cv2.inRange(hsv, lower_grn, upper_grn)	
	res = cv2.bitwise_and(frame, frame, mask = mask)

	#somthing 
	kernel = np.ones((5,5), np.uint8)	# in a 5x5 grid to look 
	erosion = cv2.erode(mask, kernel, iterations = 1)		#find single pixels in this image
	#dilation = cv2.dilate((mask, kernel, iterations = 1)		#find single pixels in this image
	
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	cv2.imshow('erosion', erosion)
	#cvs.imshow('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:				# thats ESC
		break


cv2.destroyAllWindows()
cap.release()
