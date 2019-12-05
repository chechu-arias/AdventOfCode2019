#!/usr/bin/python3

import time
import sys

def formatInput(file):
    input = list()
    with open(file,"r") as filedata:
        for line in filedata:
            input = line.replace("\n","").split(",")
    
    #Input is a list of ints
    input = list(map(int, input))

    return input

def Day2(file):

    inputL = formatInput(file)

    pos = 0
    while pos < len(inputL):
        
        repr = str(inputL[pos])

        if repr[-1] == "1" or repr[-1] == "2":
            try:
                if repr[-3] == "0":
                    val1 = inputL[inputL[pos+1]]
                else:
                    val1 = inputL[pos+1]
            except IndexError:
                val1 = inputL[inputL[pos+1]]

            try:
                if repr[-4] == "0":
                    val2 = inputL[inputL[pos+2]]
                else:
                    val2 = inputL[pos+2]
            except IndexError:
                val2 = inputL[inputL[pos+2]]

            if repr[-1] == "1":
                inputL[inputL[pos+3]] = val1 + val2
            else:
                inputL[inputL[pos+3]] = val1 * val2

            pos += 4

        elif repr[-1] == "3":

            print("TEST diagnostic program will start.\n Please input the ID of the system.")
            inputL[inputL[pos+1]] = int(input())
            pos += 2

        elif repr[-1] == "4":
            try:
                if repr[-3] == "1":
                    print(inputL[pos+1])
                else:
                    print(inputL[inputL[pos+1]])
            except IndexError:
                print(inputL[inputL[pos+1]])

            pos += 2

        elif repr[-1] == "5" or repr[-1] == "6":
            try:
                if repr[-3] == "0":
                    val1 = inputL[inputL[pos+1]]
                else:
                    val1 = inputL[pos+1]
            except IndexError:
                val1 = inputL[inputL[pos+1]]

            try:
                if repr[-4] == "0":
                    val2 = inputL[inputL[pos+2]]
                else:
                    val2 = inputL[pos+2]
            except IndexError:
                val2 = inputL[inputL[pos+2]]

            if (repr[-1] == "5" and val1 != 0) or (repr[-1] == "6" and val1 == 0):
                pos = val2
            else:
                pos += 3

        elif repr[-1] == "7" or repr[-1] == "8":
            try:
                if repr[-3] == "0":
                    val1 = inputL[inputL[pos+1]]
                else:
                    val1 = inputL[pos+1]
            except IndexError:
                val1 = inputL[inputL[pos+1]]

            try:
                if repr[-4] == "0":
                    val2 = inputL[inputL[pos+2]]
                else:
                    val2 = inputL[pos+2]
            except IndexError:
                val2 = inputL[inputL[pos+2]]

            if (repr[-1] == "7" and val1 < val2) or (repr[-1] == "8" and val1 == val2):
                inputL[inputL[pos+3]] = 1
            else:
                inputL[inputL[pos+3]] = 0
                
            pos += 4

        elif repr[-1] == "9" and repr[-2] == "9":
            print("Abort.")
            break

            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d5.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day2(file)
        print("Execution time equal to {0}".format(time.time() - startTime))