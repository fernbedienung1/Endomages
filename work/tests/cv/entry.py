#!/usr/bin/env python3

from optparse import OptionParser
from cam import CAM
###############################################################################
## VARIABLES 
###############################################################################
global device


###############################################################################
## FUNCTIONS
###############################################################################
def parseARGS():
	global device

	parser = OptionParser()
	parser.add_option("-d", "--device", action="store", type="string", dest="device",
			help="video input device", default="/dev/video0", metavar="/dev/video*")
	(options, args) = parser.parse_args()
	
	device=options.device
	
###############################################################################
## MAIN
###############################################################################
if __name__ == "__main__":
	parseARGS()
	
	cam = CAM(device)
	cam.open()
	cam.show()
