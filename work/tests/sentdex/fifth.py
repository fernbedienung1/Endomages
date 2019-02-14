#!/usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread('murcielago.jpg')
rows, cols, channel = img.shape

roi = img[0:rows, 0:cols]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray, 200,  255, cv2.THRESH_BINARY_INV)

cv2.imshow('mask', mask)
cv2.imshow('INV_mask', cv2.bitwise_not(mask))

cv2.waitKey(0)
cv2.destroyAllWindows()
