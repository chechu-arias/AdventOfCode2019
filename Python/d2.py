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

    #Part 1 problem requiriment
    #input[1] = 12
    #input[2] = 2

    return input

def Day2(file):
    inputL = formatInput(file)

    for pos1 in range(100):
        for pos2 in range(100):
            inputtry = [numb for numb in inputL]
            inputtry[1] = pos1
            inputtry[2] = pos2
            pos = 0
            while pos+4 < len(inputtry):
                if inputtry[pos] == 1:
                    inputtry[inputtry[pos+3]] = inputtry[inputtry[pos+2]] + inputtry[inputtry[pos+1]]
                elif inputtry[pos] == 2:
                    inputtry[inputtry[pos+3]] = inputtry[inputtry[pos+2]] * inputtry[inputtry[pos+1]]
                elif inputtry[pos] == 99:
                    break
                pos += 4
            
            if pos1 == 12 and pos2 == 2:
                print("Part 1 is {0}".format(inputtry))
            if inputtry[0] == 19690720:
                print("Part 2 positions are {0} and {1}.".format(pos1, pos2))
                print("Part 2 result is {0}.".format(100* pos1 + pos2))
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d2.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day2(file)
        print("Execution time equal to {0}".format(time.time() - startTime))