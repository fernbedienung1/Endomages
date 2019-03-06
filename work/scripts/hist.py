#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import argparse
import csv

# first and obligatory arguent is the picture
parser = argparse.ArgumentParser()
parser.add_argument("jpg", help="Input picture for Histogram")
parser.add_argument("-l", "--createLog", help="create csv logfile", type=str, nargs='?' )
parser.add_argument("-o", "--outFile", help="save to file instead of Display Result", type=str, nargs='?' )
parser.add_argument("-s", "--short", help="create combined Histogram instead of 3 singe channels", action="store_true")

args = parser.parse_args()


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


def __plt(blue, green, red):
    scale = range(0, 255, 1)
    plt.plot(scale, blue, 'b.', scale, green, 'g.', scale, red, 'r.')
    if args.outFile:
        plt.savefig(args.outFile, bbox_inches='tight')
    else:
        plt.show()


def __createLog(b, g, r, name):
    # This will write a file with the calculated history data 
    # will be necessary for the "OVERALL" - histogramm

    with open(name, mode='w') as csv_f:
        csvWrite= csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
        csvWrite.writerow(b)
        csvWrite.writerow(g)
        csvWrite.writerow(r)


def __hist(b, g, r):
    plt.title("Histograms of color channels")
    yaxis= max(len(b), len(g), len(r))

    blue = plt.subplot(311)
    blue.set_xlabel("Intensity of Blue Pixels")
    blue.set_ylabel("Count of Pixles")
    # blue.set_title("Blue Channel")
    blue.axis([0,255, 0, yaxis]) 
    blue.hist(b, color='b', density=1)

    green = plt.subplot(312)
    green.set_xlabel("Intensity of Green Pixels")
    green.set_ylabel("Count of Pixles")
    # green.set_title("Green Channel")
    green.axis([0,255, 0, yaxis])
    green.hist(g, color='g', density=1)

    red = plt.subplot(313)
    red.set_xlabel("Intensity of Red Pixels")
    red.set_ylabel("Count of Pixles")
    # red.set_title("Red Channel")
    red.axis([0,255, 0, yaxis]) 
    red.hist(r, color='r', density=1)


    if args.outFile:
        plt.savefig(args.outFile, bbox_inches='tight')
    else:
        plt.show()
    

def main():
    img = cv2.imread(args.jpg)

    blue, green, red = calcHist(img)

    if args.short:
        __plt(blue, green, red)
    else:
        __hist(blue, green, red)

    if args.createLog:
        __createLog(blue, green, red, args.createLog)
        print("logFile Created:\t %s" % args.createLog)


if __name__ == '__main__':
    print("-----  Histogram  -----")
    main()
