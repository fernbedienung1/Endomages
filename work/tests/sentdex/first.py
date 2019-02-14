#!/usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('murcielago.jpg', cv2.IMREAD_GRAYSCALE)

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [100,50], 'r', linewidth=5)
plt.show()
