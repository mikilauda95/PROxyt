#!/usr/bin/env python
import sys,os
import csv
import time
import argparse

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
import networkx as nx

def doArgs(argList, name):
    parser = argparse.ArgumentParser(description=name)

    parser.add_argument('-v', "--verbose", action="store_true", help="Enable verbose debugging", default=False)
    parser.add_argument('--input', action="store", dest="inputFn", type=str, help="Input file name", required=True)
    parser.add_argument('--output', action="store", dest="outputFn", type=str, help="Output file name", required=True)

    return parser.parse_args(argList)

def ReadCardsFromCSV(file_name):
    c_list = []
    fd = open(file_name)
    csvreader = csv.reader(fd)

    for c in csvreader:
        c_list.append(c)
    print(c_list)
    return c_list

def SanitizeNames(c_list):
    sanitized_list = []
    for c_row in c_list:
        sanitized_num = c_row[1]
        sanitized_name = c_row[0].lower()
        sanitized_name = sanitized_name.replace(" ", "-")
        sanitized_name = sanitized_name.replace("'", "")
        sanitized_list.append([sanitized_name, sanitized_num])

    print("Debugging SanitizeNames")
    print(sanitized_list)

    return sanitized_list

def DownloadImages(c_list):
    # Create Folder for downloading cards images
    if not os.path.exists("images"):
        os.makedirs("images")

    # Download the cards one by one from the website
    MAGIC_BASE_URL="https://www.magicspoiler.com/mtg-spoiler/"
    c_list = SanitizeNames(c_list)


def main():
    progName = "Template"
    args = doArgs(sys.argv[1:], progName)

    verbose = args.verbose
    inputFn = args.inputFn
    outputFn = args.outputFn

    print("Starting %s" % (progName))
    startTime = float(time.time())

    if not os.path.isfile(inputFn):
        print("Input doesn't exist, exiting")
        return

    outputBase = os.path.dirname(outputFn)
    if outputBase!='' and not os.path.exists(outputBase):
        print("Output directory doesn't exist, making output dirs: %s" % (outputBase))
        os.makedirs(outputBase)

    # Read Cards name from file and put them in a list for elaboration

    card_list = ReadCardsFromCSV(inputFn)

    # Search the image for each card in the list and put it in folder cards

    DownloadImages(card_list)

    # Create PDF with all cards repeated by number

    print("Finished in %0.4f seconds" % (time.time() - startTime))
    return

if __name__ == '__main__':
    #sys.argv = ["programName.py","--input","test.txt","--output","tmp/test.txt"]
    main()
