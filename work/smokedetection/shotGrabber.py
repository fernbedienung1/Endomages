#!/usr/bin/env  python3

import cv2
import time
import argparse
import os


def main(vid, outFolder):
    start = time.time()
    
    cnt = 0
    while vid.isOpened():
        print(start, end='\r') 
        cnt += 1
        ret, frame = vid.read()
        
        if ret == False:
            print ("CRITCAL ERROR IN READIN\'")
            exit(ret)

        cv2.imshow('name', frame)
        # cv2.imwrite("%s/shot_%d.jpg" % (outFolder, cnt), frame, cnt)    # this still throws erros
        
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='creats screenshots every second and writs them to given Folder')
    parser.add_argument("video", help="InputVideo")
    parser.add_argument("output", help="Foldername for Screenshots", default='screenshots')

    args = parser.parse_args()
    inFile = cv2.VideoCapture(args.video)

    if os.path.exists(args.output):
        os.rmdir(args.output)
        
    os.mkdir(args.output)
    main(inFile, args.output)
