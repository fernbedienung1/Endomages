#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import argparse
import tqdm

# first and obligatory arguent is the picture
parser = argparse.ArgumentParser()
parser.add_argument("jpg", help="Input picture for Histogram")

args = parser.parse_args()
jpg = args.jpg

# additional
outFile = "out.png"


def bw():
    # this was intended to create Black / white / greyscale images ...
    # but imagemagic does the trick here already
    for i in tqdm(range(100)):
        pass
    print("nothing to do here")

# wont work like that - call by value not call by ref


if __name__ == '__main__':
    print("-----  Contrast  -----")
    print("Input File:\t%s" % jpg)
    print
    img = cv2.imread(jpg)
    cv2.imshow("original", img)
    bw()

    while True:
        if cv2.waitKey(33) == ord('q'):
            break
            # here you could include the save button
