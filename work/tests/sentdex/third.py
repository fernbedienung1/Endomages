#!/usr/bin/env python3

import numpy as np 
import cv2
#import matplotlib.pyplot as pts

img = cv2.imread('murcielago.jpg', cv2.IMREAD_COLOR)

# parametres: img, startpoint , stoppoint, color, linewidth
cv2.line(img, (0,0), (200,200), (255,0,0), 15)
cv2.rectangle(img, (100,100), (300,300), (0,255,0), 5)
cv2.circle(img, (200,200), 25, (0,0,255), -1)	#negative linewith will fill

pts = np.array([[10,5], [20,30], [79,20], [11,11]], np.int32)
pts = pts.reshape((-1,1,2))		#reshape to 1,1,2

cv2.polylines(img, [pts], True, (255,255,0), 3)	# True interconects first and last
# this is not added?
#killit

#write into the Image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0,500), font, 1, (0,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
