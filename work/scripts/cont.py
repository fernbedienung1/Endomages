#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import argparse

# first and obligatory arguent is the picture
parser = argparse.ArgumentParser()
parser.add_argument("jpg", help="Input picture for Histogram")
# Colorthresholds
parser.add_argument("-tb", "--thresholdBlue", help="increase Blue part", type=int, choices=range(0, 127), nargs='?', default='0')
parser.add_argument("-tg", "--thresholdGreen", help="increase Green part", type=int, choices=range(0, 127), nargs='?', default='0')
parser.add_argument("-tr", "--thresholdRed", help="increase Red part", type=int, choices=range(0, 127), nargs='?', default='0')
parser.add_argument("-i", "--intensity", help="intensity for contrast enhancement", type=int, choices=range(0, 100), nargs='?', default='0')

args = parser.parse_args()
jpg = args.jpg
tb = args.thresholdBlue
tg = args.thresholdGreen
tr = args.thresholdRed
intensity = args.intensity

# additional
cont = jpg + "_CONT.png"
cont = jpg + "_CONT_HIST.png"


# wont work like that - call by value not call by ref
def add(val, inc):
    if val + inc >= 255:
        val = 255
    else:
        val = val + inc


def sub(val, inc):
    if val - inc <= 0:
        val = 0
    else:
        val = val - inc


def createContrast(img, tb, tg, tr, intensity):

    # print("first Pixel:\t%s" % (img[0][0]))
    # print("Thresholds:\nBlue:\t%s\tGreen:\t%s\tRed:\t%s" % (tb, tg, tr))
    # print("increasing of:\t%s" % intensity)

    for row in img:   # through rows
        for px in row:
            # blue
            if px[0] >= tb:
                add(px[0], intensity)
            elif px[0] <= 255-tb:
                sub(px[0], intensity)

            # green
            if px[1] >= tb:
                add(px[1], intensity)
            elif px[1] <= 255-tb:
                sub(px[1], intensity)

            # red
            if px[2] >= tb:
                add(px[2], intensity)
            elif px[2] <= 255-tb:
                sub(px[2], intensity)

    cv2.imshow("enhanced", img)


if __name__ == '__main__':
    print("-----  Contrast  -----")
    print("Input File:\t%s" % jpg)
    print
    img = cv2.imread(jpg)
    cv2.imshow("original", img)

    createContrast(img, tb, tg, tr, intensity)
    while True:
        if cv2.waitKey(33) == ord('q'):
            break
