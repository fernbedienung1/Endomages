#!/usr/bin/env	python3

import cv2
import numpy as np

#example Vid
cap = cv2.VideoCapture("../../data/rotation_640.mp4")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True :
	ret, frame = cap.read()	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for(x,y,w,h) in faces:	# he truly knows the strukture of this data
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)			#pic, start, end, color, linewidth

	cv2.imshow('original', frame)
#	cv2.imshow('mask', gray) 	##its just grey 


	k = cv2.waitKey(5) & 0xFF
	if k == 27:				# thats ESC
		break


cv2.destroyAllWindows()
cap.release()
