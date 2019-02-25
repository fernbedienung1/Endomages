#!/usr/bin/env	python3

import cv2
import numpy as np

###############################################################################
#                    Algorithms Class					      #
###############################################################################
# This one should get frames form the Video input and
# return the filtered Result as a frame


class Algorithm (object):
    # holds algorithms for Smoke / stain /etc removal

    # 	PRIVATE FUNCITONS
    ###########################################################################

    def __preConf(self, frame):
        # convertions, etc that are always needed prior to the MATH stuff
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return hsv

###############################################################################
#       PUBLIC FUNCITONS
###############################################################################

    def byColor(self, frame):
        hsv = self.__preConf(frame)

        # Try to find grey parts: in Saturation part of HSV
        lower = np.array([0, 120, 0]) 		# HSV
        upper = np.array([255, 200, 255])

        # applying mask to Frame
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        return res

    def byEqualHist(self, frame):

        # Create and fill mask with LAB
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        # l is "Lightness part"
        l, a, b = cv2.split(lab)

        # create filter
        hist = cv2.equalizeHist(l)

        # fuse lightness part back to IMG and reconvert
        img = cv2.merge((hist, a, b))
        res = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

        return res

    def byContrast(self, frame):

        # Create and fill mask with LAB
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

        # l is "Lightness part"
        l, a, b = cv2.split(lab)

        # create filter
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(4, 4))

        # apply filter to lightness part only
        cl = clahe.apply(l)

        # fuse lightness part back to IMG and reconvert
        img = cv2.merge((cl, a, b))
        res = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

        return res

    def byPrior(self, frame):
        res = self.__preConf(frame)
        return res

    def stain(self, frame):
        # stains might be determined by edges around dark patterns like Rain
        res = cv2.Canny(frame, 100, 200)
        return res

###############################################################################
# 	DEBUGGING PART
###############################################################################
    # While in development this is the Standart function to be called

    def testingMode(self, frame):
        # get a histogram and so on
        mask = []
        mask.append(frame)

        res = frame.ravel() # no idea what this does but it crashes the VM!!
        return res, mask

###############################################################################
# further Adjustments
###############################################################################


if __name__ == '__main__':
    print("contains algorithms - not meant to be run standalone")
    exit(1)
