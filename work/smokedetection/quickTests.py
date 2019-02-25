#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

jpg = "/home/m/Pictures/Rick.jpg"


def myHist(bgr_pic):
    r = []
    g = []
    b = []
    for line in bgr_pic:           # each row (or line....i actually dont care)
        for pixel in line:         # each pixel in line (or row)
            b.append(pixel[0])
            g.append(pixel[1])
            r.append(pixel[2])

    print("half done")              # keep trak of time consumpution

    hist_b = []
    hist_g = []
    hist_r = []

    for i in range(0, 255):
        hist_b.append(b.count(i))
        hist_g.append(g.count(i))
        hist_r.append(r.count(i))

    return hist_b, hist_g, hist_r


def test():
    # histogram
    img = cv2.imread(jpg)
    # hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    cv2.imshow("Original", img)

    print("original\t%s " % img[0][0])
    blue, green, red = myHist(img)      # TODO  - this needs a shitload of time
    print(blue)
    # cv2.imshow("histogram", hist)     # appearently this needs a matplot
#    plt.hist(img.ravel(), 256, [0, 256])
#    plt.show()

    while(1):
        if cv2.waitKey(5) & 0xFF == 27 or cv2.waitKey(5) & 0xFF == 113:
            break			# thats ESC or 'q'


if __name__ == '__main__':
    print("\n----- Quick and Dirty -----\n")
    test()
    print("\n")
