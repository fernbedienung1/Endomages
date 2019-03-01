#!/usr/bin/env  python3

###############################################################################
# the main purpouse of this script is to look cool (LotR - style)
# but a side effect is that it will create one gigant histogram over
# all my generated data
###############################################################################

# imports to work with files and CSV parsing
import os
import csv
from matplotlib import pyplot as plt

# global buffer variables, will be written to big histogram later
blue = [0] * 255
green = [0] * 255
red = [0] * 255


def oneFunctionToFindThem():
    # find all CSV data
    csvs = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".csv"):
                csvs.append(os.path.join(root, file))

    return csvs


def oneFunctionToRuleThemAll():
    # first write your own file
    with open("theOneCSV.csv", mode='w') as csv_f:
        csvWrite = csv.writer(csv_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWrite.writerow(blue)
        csvWrite.writerow(green)
        csvWrite.writerow(red)

    # Next up is the image creation

    scale = range(0, 255, 1)
    plt.plot(scale, blue, 'b.', scale, green, 'g.', scale, red, 'r.')
    plt.savefig("theOneJPG.jpg", bbox_inches='tight')


def oneFunctionToBindThem(files):
    # here I need to add them all up

    for data in files:
        # in every found file
        with open(data, mode='r') as csv_f:
            reader = csv.reader(csv_f, delimiter=',')
            # every found Row
            for row in reader:
                # add up All Found pixels
                if reader.line_num == 1:
                    # this is Blue
                    for cnt in range(255):
                        blue[cnt] += int(row[cnt])

                elif reader.line_num == 2:
                    # this is Green
                    for cnt in range(255):
                        green[cnt] += int(row[cnt])

                elif reader.line_num == 3:
                    # this is Red
                    for cnt in range(255):
                        red[cnt] += int(row[cnt])


if __name__ == "__main__":
    files = oneFunctionToFindThem()
    oneFunctionToBindThem(files)
    oneFunctionToRuleThemAll()
