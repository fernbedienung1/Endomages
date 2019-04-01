#!/bin/bash
# check if used right
if [ $# -eq 0 ]; then
	echo "not enought args - I need the caputre time"
	exit 1
fi

# Command to capture from Webcam and write to file locally
avconv -f video4linux2 -framerate 30 -video_size 1280x720 -t $1 -i /dev/video0 "WEBCAM_$(date +%F_%R).MOV"
