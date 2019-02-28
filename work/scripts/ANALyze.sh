#!/bin/bash


stage1(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 1 ____\n"
    printf "__________________________\n\n"
    printf "creating shots of every second\n"
    
    # this should take a while....
    for i in *.mp4; do grabber $i -o OUT/vid\_$i; done
}

stage2(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 2 ____\n"
    printf "__________________________\n\n"
    printf "creating histograms of every shot\n"

    # better create some loggin for all the pixel values....
    # will take time... will take space .... monitore it with "time" and "space" (lol)

    # tools:    time $(toolname)
    #           htop -p PID

    # TOOL: psrecord (python va pip)

}

stage3(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 3 ____\n"
    printf "__________________________\n\n"

    printf "create ONE histogramm of ALL shots"
}
##########################   MAIN   ###########################################
printf "starting to analyze ALL VIDEOS\n"
printf "   expect this to take forever\n"
printf ""

stage1

stage2

stage3


printf "_____ FINALLY DONE ______\n" 

