#!/usr/bin/env  python3

import cv2
import time
import argparse


def main(vid, outFolder):
    start = time.time()
    _, frame = vid.read()

    print(start)
    #TODO - make this thing create screenshots - 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='creats screenshots every second and writs them to given Folder')
    parser.add_argument("video", help="InputVideo")
    parser.add_argument("output", help="Foldername for Screenshots", default='screenshots')

    args = parser.parse_args()
    inFile = cv2.VideoCapture(args.video)

    main(inFile, args.output)
