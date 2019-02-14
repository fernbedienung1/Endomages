#!/usr/bin/env	python3

#library imports
import cv2
import time
import argparse

#file imports
from algorithms import Algorithm

###############################################################################
#### ARG Parsing
###############################################################################
parser = argparse.ArgumentParser()
parser.add_argument("videoFile", help="video to remove smoke from")
parser.add_argument("-v", "--verbose", help="Debug output on", action="store_true")
parser.add_argument("-o", "--output", help="specify output file name for Resulting Video [MP4]")
parser.add_argument("-t", "--type", help="specify removal Algorithm", type=str, choices=['color','contrast','prior','detect','edge','test'], default='test')	#test is for debugging
#parser.add_argument("-r", "--remove", help="Targeted noise to remove", type=str, choices=['smoke','steam','staining','all'], default='smoke')
parser.add_argument("-f", "--framerate", help="display Framrate", action="store_true")

args = parser.parse_args()

#Verbose arg
if args.verbose:
	print("using video:\t\t%s" % args.videoFile)
	if args.output	: print("Writingto:\t\t%s.mp4" % args.output) 
	if args.type	: print("FilterType:\t\t%s" % args.type)
	#if args.remove 	: print("TargetNoise:\t\t%s" % args.remove)

#OUTPUT FILE
if args.output :
	#out of convenience we will always create mp4 vids
	frame_width = int(cap.get(3))
	frame_height= int(cap.get(4))
	out = cv2.VideoWriter(args.output + ".mp4",cv2.VideoWriter_fourcc('M','P','4','V'), 10, (frame_width,frame_height))


###############################################################################
## MAIN 
###############################################################################
cap = cv2.VideoCapture(args.videoFile)
algo = Algorithm()

while True :
	
	
	ret, frame = cap.read()	# python _ --> not used
	if type(frame) == type(None): break	# stop execution when video is over
	#timestamp for Framerate
	if args.framerate : last_time=time.time()
###############################################################################

	# Algorithm selection
	if args.type == 'color':			# Determine Used algorithm
		res = algo.byColor(frame)

	elif args.type == 'contrast' :
		res = algo.byContrast(frame)

	elif args.type == 'prior' :
		res = algo.byPrior(frame)

	elif args.type == 'detect' :
		res = algo.byPrior(frame)

	elif args.type == 'test' : 
		res, mask = algo.testingMode(frame)
		n = 0                                   #just to name the frames
		for i in mask :
			cv2.imshow('stage_'+str(n), i)	#Intermediate steps
			n += 1

	elif args.type == 'edge' : 
                res = algo.canny(frame)

	# Compare Origian to Result
	cv2.imshow('Input', frame)			#Original Input Frame
	cv2.imshow('Filtered', res)			#Cretated Output


###############################################################################

	# Write result to file if specified
	if args.output: out.write(res)

	# output Framerate 
	if args.framerate : print("FPS:\t%.2f" % (1/ (time.time() - last_time)), end='\r')

	# check if user interrupts using ESC
	if cv2.waitKey(5) & 0xFF == 27 or cv2.waitKey(5) & 0xFF == 113:		break			# thats ESC or 'q'

	if cv2.waitKey(5) & 0xFF == 32 : 				#Play / Pause funktion
		while True:
			if cv2.waitKey(5) & 0xFF == 32 : 
				break	# resume


#Cleanup after video is done
cap.release()
cv2.destroyAllWindows()
