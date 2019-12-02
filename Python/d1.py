#!/usr/bin/python3

import time
import sys

def Day1(file):
    res = 0
    aux = 0
    with open(file,"r") as input:
        for line in input:
            mass = int(line)
            fuel = (mass//3) - 2
            #Part 1 calculating the fuel necessary
            res += fuel
            #Part 2 adding the fuel necessary for the fuel necessary and so on
            while ((fuel//3)-2) > 0:
                fuel = ((fuel//3)-2)
                aux += fuel

    print("Part 1 is {0}".format(res))
    print("Part 2 is {0}".format(aux+res))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d1.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day1(file)
        print("Execution time equal to {0}".format(time.time() - startTime))