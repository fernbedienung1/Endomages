#!/usr/bin/env  python3

import cv2
import time
import argparse
import shutil
import os


def main(inFile, outFolder):
    vid = cv2.VideoCapture(inFile)

    cnt = 0
    start = time.time()
    while vid.isOpened():
        ret, frame = vid.read()
        if type(frame) == type(None):
            break

        cv2.imshow('name', frame)

        if start + 1 <= time.time():
            cv2.imwrite("%s/shot_%d.jpg" % (outFolder, cnt), frame)
            print("Writing:\t%s/%s_%d.jpg" % (outFolder,inFile, cnt))
            cnt += 1
            start = time.time()

        if cv2.waitKey(5) & 0xFF == 27 or cv2.waitKey(5) & 0xFF == 113:
            break			# thats ESC or 'q'

    vid.release()


# This makes only the Parsing, actual "inteligence" happens above
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='creats screenshots every second and writs them to given Folder')
    parser.add_argument("video", help="InputVideo")
    parser.add_argument("-o", "--output", help="specify output directory name for Resulting Video [MP4]", default='Screenshots')

    args = parser.parse_args()

    if os.path.exists(args.output):     # remove the folder if i was lazy
        shutil.rmtree(args.output)

    os.mkdir(args.output)
    main(args.video, args.output)

    cv2.destroyAllWindows()
