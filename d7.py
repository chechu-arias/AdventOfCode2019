#!/usr/bin/python3

import time
import sys
import itertools

def formatInput(file):
    input = list()
    with open(file,"r") as filedata:
        for line in filedata:
            input = line.replace("\n","").split(",")
    
    #Input is a list of ints
    input = list(map(int, input))

    return input

def Intcode_computer(inputL, inputNum, inputPrevAmp):
    pos = 0
    contInputFunc = 0
    while pos < len(inputL):
        
        repr = str(inputL[pos])

        if repr[-1] in ["1", "2","5","6","7","8"]:
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
            elif repr[-1] == "2":
                inputL[inputL[pos+3]] = val1 * val2
            elif repr[-1] in ["5", "6"]:
                if (repr[-1] == "5" and val1 != 0) or (repr[-1] == "6" and val1 == 0):
                    pos = val2
                else:
                    pos += 3  
            elif (repr[-1] == "7" and val1 < val2) or (repr[-1] == "8" and val1 == val2):
                inputL[inputL[pos+3]] = 1
            else:
                inputL[inputL[pos+3]] = 0

            if repr[-1] in ["1", "2", "7", "8"]:
                pos += 4

        elif repr[-1] == "3":
            if contInputFunc == 0:
                inputL[inputL[pos+1]] = inputNum
            else:
                inputL[inputL[pos+1]] = inputPrevAmp
            contInputFunc += 1
            pos += 2

        elif repr[-1] == "4":
            res = 0
            try:
                if repr[-3] == "1":
                    res = inputL[pos+1]
                else:
                    res = inputL[inputL[pos+1]]
            except IndexError:
                res = inputL[inputL[pos+1]]
            
            pos += 2
            return res

        elif repr[-1] == "9" and repr[-2] == "9":
            print("Abort.")
            break

def Day7(file):

    inputL = formatInput(file)

    n_amplif = 5
    values_part1 = []
    for i in range(n_amplif):
        values_part1.append(i)
    

    returnvals = list()
    for perm_tup in itertools.permutations(values_part1):
        perm = list(perm_tup)
        amp_val = 0
        for pos in range(len(perm)):
            if pos == 0:
                amp_val = Intcode_computer(inputL, perm[pos], 0)
            else:
                amp_val = Intcode_computer(inputL, perm[pos], amp_val)
        returnvals.append(amp_val)
    
    print("El valor máximo devuelto es de {0}".format(max(returnvals)))
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d7.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day7(file)
        print("Execution time equal to {0}".format(time.time() - startTime))