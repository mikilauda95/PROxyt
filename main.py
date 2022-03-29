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

    # Create PDF with all cards repeated by number

    print("Finished in %0.4f seconds" % (time.time() - startTime))
    return

if __name__ == '__main__':
    #sys.argv = ["programName.py","--input","test.txt","--output","tmp/test.txt"]
    main()
