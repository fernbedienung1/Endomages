#!/bin/bash

##########################################################
# This one will stream a Webcam over the network - Unencrypted
##########################################################

#avconv -f video4linux2 -s 1280x960 -i /dev/video0 -f avi pipe: | nc -lkp 60100
# this one is for the "server"


#This one is for the client
nc 192.168.137.33 60100 | ffmpeg -i - $(date +%F_%R).mp4
