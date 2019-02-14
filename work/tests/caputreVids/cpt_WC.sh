#!/bin/bash
if [ $# -eq 0 ]; then
	echo "not enought args - I need the caputre time"
	exit 1
fi

avconv -f video4linux2 -framerate 30 -video_size 1280x720 -t $1 -i /dev/video0 "WEBCAM_$(date +%F_%R).MOV"
