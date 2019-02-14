#!/usr/bin/env	python3

import cv2
import numpy as np

#example Vid
cap = cv2.VideoCapture("../../data/rotation_640.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()




while True :
	ret, frame = cap.read()	# python _ --> not used
	fgmask = fgbg.apply(frame)

	# remove unwanted background pixels

	cv2.imshow('original', frame)
	cv2.imshow('mask', fgmask)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:				# thats ESC
		break


cv2.destroyAllWindows()
cap.release()
