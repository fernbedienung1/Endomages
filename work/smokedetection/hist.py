#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import argparse

# first and obligatory arguent is the picture
parser = argparse.ArgumentParser()
parser.add_argument("jpg", help="Input picture for Histogram")
args = parser.parse_args()
jpg = args.jpg
# TODO - add switch for fileoutput / screenoutput

# more globals
output = jpg + "_HIST.png"


def calcHist(bgr_pic):
    r = []
    g = []
    b = []
    
    # split up the image
    for line in bgr_pic:           # each row (or line....i actually dont care)
        for pixel in line:         # each pixel in line (or row)
            b.append(pixel[0])
            g.append(pixel[1])
            r.append(pixel[2])

    hist_b = []
    hist_g = []
    hist_r = []

    # Smaller images speed things up ... but also change the result 
    for i in range(255):            # This one takes a fuckload of time..
        hist_b.append(b.count(i))
        hist_g.append(g.count(i))
        hist_r.append(r.count(i))
        print("%s / 255" % i, end='\r')

    return hist_b, hist_g, hist_r


def __showPlt(blue, green, red):
    scale = range(0, 255, 1)
    plt.plot(scale, blue, 'b.', scale, green, 'g.', scale, red, 'r.')
    plt.savefig(output, bbox_inches='tight')


def __showHist(blue, green, red):
    plt.figure(1)

    # Blue
    plt.subplot(311)
    plt.hist(blue, color='b')
    plt.plot()

    # Green
    plt.subplot(321)
    plt.hist(green, color='g')
    plt.plot()

    # Red
    plt.subplot(331)
    plt.hist(red, color='r')
    plt.plot()

    # common stuff
    plt.title(jpg)


def main():
    img = cv2.imread(jpg)

    blue, green, red = calcHist(img)

    __showPlt(blue, green, red)
    __showHist(blue, green, red)


if __name__ == '__main__':
    print("-----  Histogram  -----")
    print("Input File:\t%s" % jpg)
    print("OutputFile:\t%s" % output)
    main()
    print("\n")
