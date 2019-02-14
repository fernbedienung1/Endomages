#!/usr/bin/env	python3

import cv2
import numpy as np


#Thresholds

img = cv2.imread('murcielago.jpg')

	# 12 - below bekomms white  -over it gets dark
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#gausian threshold 		Appearantly this one works great with shaddows in real images
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#OTSU
retval2, otsu= cv2.threshold(grayscaled, 123, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('thresh', threshold)
cv2.imshow('gray',grayscaled)
cv2.imshow('GAUS',gaus)
cv2.imshow('OTSU', otsu)


cv2.waitKey(0)
cv2.destroyAllWindows() 
