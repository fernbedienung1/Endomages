#!/bin/bash


MADDR="maximilianhei92@gmail.com"

stage1(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 1 ____\n"
    printf "__________________________\n\n"
    printf "creating shots of every second\n"
    
    mkdir OUT
    # this should take a while....
    for i in *.mp4; do
        grabber $i -o OUT/vid\_$i           # Actual work happenes here 
        if [ $? -ne 0 ] ; then    
            printf "FILE:%s \n\n Screenshot creation returned a non Zero Exit Value! \n" $i | mail $MADDR -s "[WARNING] - Screenshot creation" & 
        fi
    done

    printf "SCREENSHOT CREATION [DONE]:\t\t%s\n" $(date +%F_%T) >> TimeLog.txt
}


stage2(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 2 ____\n"
    printf "__________________________\n\n"
    printf "creating histograms of every shot\n"

    # THIS SECTION WILL TAKE A SHITLOAD OF TIME!!
    # NOW everything should be in the folder OUT with sub-folders for every Video.

    cd OUT/     # will this work within scripts?

    for i in ./*/*.jpg; do 
        gram $i;        # This command does the actual work
        if [ $? -ne 0 ] ; then    
            printf "FILE:%s \n\n Histogramm creation returned a non Zero Exit Value! \n" $i | mail $MADDR -s "[WARNING] - Screenshot creation" & 
        fi
    done

    cd ..       #Go back up when done

    printf "HISTOGRAMM CREATION [DONE]:\t\t%s\n" $(date +%F_%T) >> TimeLog.txt
}


stage3(){
    printf "__________________________"
    printf "\n____ STARTING STAGE 3 ____\n"
    printf "__________________________\n\n"

    printf "create ONE histogramm of ALL shots"

    # this will search through the directories for CSV files
    # then cummulates them and creates a overall output
    ring                # doesn't even need a parameter =D

    printf "Cumulative HISTOGRAM [DONE]:\t%s\n" $(date +%F_%T) >> TimeLog.txt
}


##########################   MAIN   ###########################################
printf "starting to analyze ALL VIDEOS\n"
printf "   expect this to take forever\n"
printf "start at\t%s\n" $(date +%F_%T)

stage1
printf "SCREENSHOT GENERATION\n\n\t [[SUCCESS]]" | mail $MADDR -s "[INFO] - DONE STAGE_I - Screenshot generation" &

# the most time intense one should be this here.
stage2
printf "HISTOGRAMM GENERATION\n\n\t [[SUCCESS]]" | mail $MADDR -s "[INFO] - DONE STAGE_II - Histogramm generation" &

stage3
printf "EVERY GENERATION\n\n\t [[SUCCESS]]" | mail $MADDR -s "[INFO] - DONE STAGE_III - Execution ended Successfully!!" &

printf "_____ FINALLY DONE ______\n" 
printf "finished at\t%s\n" $(date +%F_%T)
