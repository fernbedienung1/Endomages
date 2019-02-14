#!/usr/bin/env python3.6

import cv2
import numpy
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--Device", action="store", type="int", dest="device", 
			help="select cam", default=0) 

(options, args) = parser.parse_args()


print("using camera %d" % options.device )
cap = cv2.VideoCapture(options.device)

go = True
while(go) :
	ret, frame = cap.read()
	
	# play with the image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # GREY 
	flip = cv2.flip(frame, 0)			# upside down	
	invert = cv2.bitwise_not(frame)
	# Display the result
	cv2.imshow('CAMERA_GRAY', gray)
	cv2.imshow('CAMERA_ORIG', frame)
	cv2.imshow('CAMERA_FLIP', flip)
	cv2.imshow('CAMERA_INV', invert)
	key = cv2.waitKey(1) &0xFF
	if key == ord('q'):
		go = False
''' opens all the windows in every loop agian =D
	if key == ord('1'):
		cv2.destroyWindow('CAMERA_GRAY')
	if key == ord('2'):
		cv2.destroyWindow('CAMERA_ORIG')
	if key == ord('3'):
		cv2.destroyWindow('CAMERA_FLIP')
	if key == ord('4'):
		cv2.destroyWindow('CAMERA_INV')
'''	
cap.release()	# give cam Free

cv2.destroyAllWindows()
