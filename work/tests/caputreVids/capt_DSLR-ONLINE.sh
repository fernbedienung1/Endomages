#!/bin/bash
##########################################################
# This one will stream a Video from a DSLR to the Network - unencrypted!
##########################################################



# on the Client
#gphoto2 --capture-movie --stdout | nc -lkp 60100

nc 192.168.137.33 60100 | ffmpeg -i - $(date +%F_%R).mp4
