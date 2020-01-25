#!/usr/bin/python3

import time
import sys
import numpy as np

"""def maxMovEnDir(wire):
    conts = list()
    R = 0
    L = 0
    U = 0
    D = 0
    for mov in wire:
        if mov[0] == "L":
            L += int(mov[1:])
        elif mov[0] == "R":
            R += int(mov[1:])
        elif mov[0] == "U":
            U += int(mov[1:])
        elif mov[0] == "D":
            D += int(mov[1:])
        else:
            print("Error {0}".format(mov))
    conts.append(R)
    conts.append(L)
    conts.append(D)
    conts.append(U)
    maxVal = max(conts)
    #print("Max value is: {0}".format(maxVal))
    #print("Vals are left: {0}, right: {1}, up: {2} and down: {3}".format(L, R, U, D))
    return maxVal"""

def fillDictWithWire(input, coinc, wire, num, part, dists):
    if part == 2:
        cont = 0
    x = 0
    y = 0
    for mov in wire:
        cant = int(mov[1:])
        for i in range(cant+1):
            key = (x,y)
            ins = input.get(key,0)
            if part == 2:
                steps = cont + i
            if ins == 0:
                if part == 1:
                    input[key] = num
                else:
                    input[key] = num
                    dists[key] = steps
            elif num == 2 and (key[0] != 0 or key[1] != 0):
                if ins == 1:
                    if part == 1:
                        coinc.append(key)
                    else:
                        coinc.append((dists[key], steps))
            if i != cant:
                if mov[0] == "L":
                    x -= 1
                elif mov[0] == "R":
                    x += 1
                elif mov[0] == "U":
                    y += 1
                elif mov[0] == "D":
                    y -= 1
        if part == 2:
            cont += cant

def calculateDist(coinc):
    res = list()
    for coord in coinc:
        aux = abs(coord[0]) + abs(coord[1])
        res.append(aux)
    return res



def Day3(file, part):

    data = list()
    input = dict()
    dists = dict()

    with open(file,"r") as filedata:
        for line in filedata:
            data.append(line)
    wire1 = data[0].replace("\n", "").split(",")
    wire2 = data[1].replace("\n", "").split(",")

    coinc = list()

    fillDictWithWire(input, coinc, wire1, 1, part, dists)
    fillDictWithWire(input, coinc, wire2, 2, part, dists)

    Manhattan_dist = calculateDist(coinc)
    if part == 1:
        print("Minimum value of manhattan is {0}".format(min(Manhattan_dist)))
    else:
        print("Minimum value of steps is {0}".format(min(Manhattan_dist)))

    return input

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 d3.py inputpath {1|2}")
    else:
        file = sys.argv[1]
        part = int(sys.argv[2])
        startTime = time.time()
        Day3(file, part)
        print("Execution time equal to {0}".format(time.time() - startTime))