#!/usr/bin/env  python3

import os


def oneFunctionToFindThem():
    # find all CSV data
    files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".csv"):
                files.append(os.path.join(root, file))

    return files


def oneFunctionToRuleThemAll():
    print("even Nicer")


def oneFunctionToBindThem(files):
    print("blabla")
    # here I need to add them all up


if __name__ == "__main__":
    files = oneFunctionToFindThem()
    print(files)
    # oneFunctionToBindThem(files)
    # oneFunctionToRuleThemAll()
