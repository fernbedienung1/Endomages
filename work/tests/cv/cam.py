#!/usr/bin/env python3
import cv2
#import numpy as np

class CAM():
	__dev="0"
	__cam=None
	
	def __init__(self, src):
		print("CV2-Version\t%s" % cv2.__version__)
		print("using:\t%s" % src)
		__dev=[int(s) for s in str.split(src) if s.isdigit()]

	def __del__(self):
		#self.__cam.release()
		cv2.destroyAllWindows()

	def open(self):
		self.__cam=cv2.VideoCapture(self.__dev)
		
	def show(self):
		go = True
		while(go):
			#first grab a FRAME
			ret = False
			while(not ret) :
				ret, frame = self.__cam.read() 
				pass		# somehow the camera will not get ready...
			canny = cv2.Canny(frame, 100, 200)
			cv2.imshow('CAN GET CANNY', canny)
			key = cv2.waitKey(1) &0xFF
			if key == ord('q'):
				go = False

if __name__ == "__main__" :
	print("this is not meant to be run")
