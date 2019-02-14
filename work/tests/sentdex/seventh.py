#!/usr/bin/env	python3

import cv2
import numpy as np

# img = cv2.imread('murcielago.jpg')
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("praesi.mp4")



while True :
	_, frame = cap.read()	# python _ --> not used
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# use unique color		in this case I am looking for my Green HAIR
	lower_grn = np.array([50, 40, 0]) 		#they are already HSV
	upper_grn = np.array([100, 255, 255])

	mask = cv2.inRange(hsv, lower_grn, upper_grn)	
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:				# thats ESC
		break


cv2.destroyAllWindows()
cap.release()
