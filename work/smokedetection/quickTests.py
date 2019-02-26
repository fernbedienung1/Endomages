#!/usr/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

jpg = "/home/m/Pictures/Rick.jpg"
# jpg = "/home/m/Pictures/miniRick.jpg"


def calcHist(bgr_pic):
    r = []
    g = []
    b = []
    for line in bgr_pic:           # each row (or line....i actually dont care)
        for pixel in line:         # each pixel in line (or row)
            b.append(pixel[0])
            g.append(pixel[1])
            r.append(pixel[2])

    hist_b = []
    hist_g = []
    hist_r = []

    # Could be improoved by converting the image down...should not have to much
    # effect since all pixles would disappear equally?
    for i in range(255):            # This one takes a fuckload of time..
        hist_b.append(b.count(i))
        hist_g.append(g.count(i))
        hist_r.append(r.count(i))
        print("%s / 255" % i)

    return hist_b, hist_g, hist_r


def showPlt(blue, green, red):
    scale = range(0, 255, 1)
    plt.plot(scale, blue, 'b.', scale, green, 'g.', scale, red, 'r.')
    plt.show()


def showHist(blue, green, red):
    plt.figure(1)

    # Blue
    plt.subplot(311)
    plt.hist(blue, color='b')
    plt.subtitle('Blue')
    plt.plot()

    # Green
    plt.subplot(321)
    plt.hist(green, color='g')
    plt.subtitle('Green')
    plt.plot()

    # Red
    plt.subplot(331)
    plt.hist(red, color='r')
    plt.subtitle('Red')
    plt.plot()

    plt.title(jpg)
    plt.show()


def test():
    img = cv2.imread(jpg)

    blue, green, red = calcHist(img)

    showPlt(blue, green, red)
    showHist(blue, green, red)

#    cv2.imshow("Original", img)
    while(1):
        if cv2.waitKey(5) & 0xFF == 27 or cv2.waitKey(5) & 0xFF == 113:
            break			# thats ESC or 'q'


if __name__ == '__main__':
    print("\n----- Quick and Dirty -----\n")
    test()
    print("\n")
