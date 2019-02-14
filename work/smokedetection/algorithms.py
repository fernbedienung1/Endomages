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

    def byContrast(self, frame):
        res = self.__preConf(frame)
        return res

    def byPrior(self, frame):
        res = self.__preConf(frame)
        return res

    def canny(self, frame):
        res = cv2.Canny(frame, 100, 200)
        return res

###############################################################################
# 	DEBUGGING PART
###############################################################################
    def testingMode(self, frame):
        # acutally this time i try to create contrast
        mask = []
        mask.append(cv2.cvtColor(frame, cv2.COLOR_BGR2LAB))
        l, a, b = cv2.split(mask[0])

        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(4, 4))
        cl = clahe.apply(l)		# reduce contrast

        limg = cv2.merge((cl, a, b))
        mask.append(limg)

        res = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        return res, mask

    def detect(self, frame):
        res = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return res


###############################################################################
# further Adjustments
###############################################################################
if __name__ == '__main__':
    print("contains algorithms - not meant to be run standalone")
    exit(1)
