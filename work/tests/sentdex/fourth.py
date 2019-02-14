#!/usr/bin/env python3


import numpy as np
import cv2

img = cv2.imread('murcielago.jpg', cv2.IMREAD_COLOR)

img[55,55] = [0,0,0]
px = img[55,55]


img[100:150, 100:150] = [0,0,0]


stuff = img[300:500, 300:500]
img[0:200, 0:200] = stuff


# end this
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()




