#!/usr/bin/python3

import time
import sys

def part1(input, size):
    with open(file,"r") as filedata:
        for line in filedata:
            if line.startswith("deal with"):
                
                line = line.replace("deal with increment ","")
                try:
                    incr = int(line)
                except TypeError:
                    assert "Deal with error"
                    print(line)
                
                aux = [-1] * size
                aux[0] = input.pop(0)
                pos = incr
                while len(input) > 0:
                    if aux[pos] == -1:
                        aux[pos] = input.pop(0)
                    pos = (pos+incr)%size

                input = aux

            elif line.startswith("deal into"):
                
                input.reverse()

            elif line.startswith("cut"):
                
                line = line.replace("cut ","")
                try:
                    indic = int(line)
                except TypeError:
                    assert "Cut error"
                    print(line)

                if indic > 0:
                    aux = input[:indic]
                    input = input[indic:] + aux
                else:
                    aux = input[indic:]
                    input = aux + input[:indic]
                    
    return input

def Day22():

    input = list()
    for i in range(10007):
        input.append(i)
    size = len(input)

    input = part1(input, size)
    
    for pos in range(len(input)):
        if input[pos] == 2019:
            print("El resultado de la parte 1 es: %d" % pos)
        



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d22.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day22()
        print("Execution time equal to {0}".format(time.time() - startTime))