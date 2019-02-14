#!/usr/bin/env python3.6
import cv2
import numpy

print(cv2.__version__)

imgPath = "/home/m/Pictures/"
imgGonzo = "gonzo.png"
imgBat= "murcielago.jpg"
imgG = cv2.imread(imgPath+imgGonzo, 0)		#0 parameter makes it load in greyscale
imgB = cv2.imread(imgPath+imgBat)

cv2.imshow('GONZO', imgG)
cv2.imshow('BAT', imgB)
key = cv2.waitKey(0) & 0xFF
if key == ord('a') :
	cv2.destroyWindow('BAT')
elif key == ord('b') : 
	cv2.destroyWindow('GONZO')
elif key == ord('q') :
	cv2.destroyAllWindows()

# tje 0xFF shit is because of my system is 64bit
key = cv2.waitKey(0) & 0xFF
