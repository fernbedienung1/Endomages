#!/bin/bash
# check if used right
if [ $# -eq 0 ]; then 
	echo "no ARGS supplied - but I need the CAPTURE - TIME"
	exit 1
fi

#DSLR command to start recording and save locally
gphoto2 --set-config movie=1 --wait-event=$1s --set-config movie=0 --wait-event-and-download=2s  --filename="DSLR_$(date +%F_%R).MOV"
