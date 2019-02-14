#!/usr/bin/env python3

###############################################################################
## Imports 
###############################################################################
import npyscreen
import cv2
from optparse import OptionParser
from threading import Thread
###############################################################################
## VARIABLES 
###############################################################################

## GLOBAL log file
global log	#logfile

## Input Parameters
global logFile
global headless
global camDev

###############################################################################
## FUNCTIONS 
###############################################################################
def init():
	#explicit declare that we WANT to change them!
	global logFile
	global headless
	global camDev
	global log

	parser = OptionParser()
	parser.add_option("-l", "--log", action="store", type="string", dest="logFile",
				help="logfile name", default="out.log", metavar="FILE")	
	parser.add_option("--headless", action="store_true", dest="headless",
				help="run without the TUI", default=False) 
	parser.add_option("-i", "--input", action="store", type="int", dest="camDev",
				help="camera to use", default=0)
	
	(options, args) = parser.parse_args()
	logFile=options.logFile
	headless=options.headless
	camDev=options.camDev

	log = open(logFile, 'w')			#create a logfile 
	print("---------- START ----------", file=log)

	print("encoutnered ARGS:", file=log)
	print("headless:\t%s"%(headless), file=log)
	print("logging to:\t%s"%(logFile), file=log)
	print("Camera Arg:\t/dev/video%d"%(camDev), file=log)

###############################################################################
##  Classes
###############################################################################

###############################  OpenCV  ######################################

class camControl():
	def __init__(self, camNum=0):	
		self.cap = cv2.VideoCapture(camNum)	
		print("[Cam] created:\tDevice%d" % (camNum), file=log)

	def __del__(self):	
		cv2.release()

	def go(self):
		go = True
		while(go):	
			ret, frame = self.cap.read()
			cv2.imshow('ORIGINAL',frame)
			cv2.imshow('INVERTED', cv2.bitwise_not(frame))
			key = cv2.waitKey(1) &0xFF
			if key == ord('q'):
				go = False


#################################  GUI  #######################################

class TUI(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm('MAIN', menu, name="Camera Control Center")


class menu(npyscreen.ActionForm):
	def activate(self):
		self.edit()
		self.parentApp.setNextForm(None)

	def create(self):
		self.CamNr = self.add(npyscreen.TitleSelectOne, max_height=5, value= [1], name="Seclect Camera",
				values = [ "Internal", "USB", "Endoscope"], scroll_exit=True)
	
	def on_ok(self):
		action=camControl(self.CamNr)
		cvThread= Thread(target = action.go)
		cvThread.start()
		action.go()
	
	def on_cancel(self):
		print("CANCELD by USER", file=log)
		exit()


###############################################################################
## MAIN 
###############################################################################
if(__name__ == "__main__") : 
	init()	
	if(not headless) :
		npyscreen.wrapper(TUI().run()) 				#start the TUI
	#cvThread.join()
	else :
		action=camControl(camDev)
		action.go()
	print("----------  END  ----------", file=log)
	log.close()
