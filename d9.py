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

def Intcode_computer(inputL):
    mem = dict()
    pos = 0
    despl_rel = 0
    while pos < len(inputL):
        
        repr = str(inputL[pos])
        if repr[-1] in ["1", "2","5","6","7","8"]:

            if len(repr) > 2:
                is_rel_param1 = False
                try:
                    if repr[-3] == "0":
                        val1 = inputL[inputL[pos+1]]
                    elif repr[-3] == "1":
                        val1 = inputL[pos+1]
                    elif repr[-3] == "2":
                        is_rel_param1 = True
                        val1 = inputL[inputL[pos+1]+despl_rel]
                except IndexError:
                    if is_rel_param1:
                        val1 = mem.get(inputL[pos+1]+despl_rel,0)
                    else:
                        val1 = mem.get(inputL[pos+1],0)
            else:
                val1 = inputL[inputL[pos+1]]

            if len(repr) > 3:
                is_rel_param2 = False
                try:
                    if repr[-4] == "0":
                        val2 = inputL[inputL[pos+2]]
                    elif repr[-4] == "1":
                        val2 = inputL[pos+2]
                    elif repr[-4] == "2":
                        is_rel_param2 = True
                        val2 = inputL[inputL[pos+2]+despl_rel]
                except IndexError:
                    if is_rel_param2:
                        val2 = mem.get(inputL[pos+2]+despl_rel,0)
                    else:
                        val2 = mem.get(inputL[pos+2],0)
            else:
                val2 = inputL[inputL[pos+2]]

            is_rel = False
            if repr[-1] == "1":
                try:
                    if repr[-5] == "0":
                        inputL[inputL[pos+3]] = val1 + val2
                    elif repr[-5] == "2":
                        is_rel = True
                        inputL[inputL[pos+3]+despl_rel] = val1 + val2
                except IndexError:
                    try:
                        if is_rel:
                            inputL[inputL[pos+3]+despl_rel] = val1 + val2
                        else:
                            inputL[inputL[pos+3]] = val1 + val2
                    except IndexError:
                        if is_rel:
                            mem[inputL[pos+3]+despl_rel] = val1 + val2
                        else:
                            mem[inputL[pos+3]] = val1 + val2

            elif repr[-1] == "2":
                try:
                    if repr[-5] == "0":
                        inputL[inputL[pos+3]] = val1 * val2
                    elif repr[-5] == "2":
                        is_rel = True
                        inputL[inputL[pos+3]+despl_rel] = val1 * val2
                except IndexError:
                    try:
                        if is_rel:
                            inputL[inputL[pos+3]+despl_rel] = val1 * val2
                        else:
                            inputL[inputL[pos+3]] = val1 * val2
                    except IndexError:
                        if is_rel:
                            mem[inputL[pos+3]+despl_rel] = val1 * val2
                        else:
                            mem[inputL[pos+3]] = val1 * val2
            elif repr[-1] in ["5", "6"]:
                if (repr[-1] == "5" and val1 != 0) or (repr[-1] == "6" and val1 == 0):
                    pos = val2
                else:
                    pos += 3  
            elif (repr[-1] == "7" and val1 < val2) or (repr[-1] == "8" and val1 == val2):
                try:
                    if repr[-5] == "0":
                        inputL[inputL[pos+3]] = 1
                    elif repr[-5] == "2":
                        is_rel = True
                        inputL[inputL[pos+3]+despl_rel] = 1
                except IndexError:
                    try:
                        if is_rel:
                            inputL[inputL[pos+3]+despl_rel] = 1
                        else:
                            inputL[inputL[pos+3]] = 1
                    except IndexError:
                        if is_rel:
                            mem[inputL[pos+3]+despl_rel] = 1
                        else:
                            mem[inputL[pos+3]] = 1
            else:
                try:
                    if repr[-5] == "0":
                        inputL[inputL[pos+3]] = 0
                    elif repr[-5] == "2":
                        is_rel = True
                        inputL[inputL[pos+3]+despl_rel] = 0
                except IndexError:
                    try:
                        if is_rel:
                            inputL[inputL[pos+3]+despl_rel] = 0
                        else:
                            inputL[inputL[pos+3]] = 0
                    except IndexError:
                        if is_rel:
                            mem[inputL[pos+3]+despl_rel] = 0
                        else:
                            mem[inputL[pos+3]] = 0

            if repr[-1] in ["1", "2", "7", "8"]:
                pos += 4

        # Lee input y lo mete en memoria
        elif repr[-1] == "3":

            print("Introduzca valor de Input.")

            val = int(input())
            is_rel = False
            
            try:
                if repr[-3] == "0":
                    inputL[inputL[pos+1]] = val
                elif repr[-3] == "2":
                    is_rel = True
                    inputL[inputL[pos+1]+despl_rel] = val
            except IndexError:
                try:
                    if is_rel:
                        inputL[inputL[pos+1]+despl_rel] = val
                    else:
                        inputL[inputL[pos+1]] = val
                except IndexError:
                    if is_rel:
                        mem[inputL[pos+1]+despl_rel] = val
                    else:
                        mem[inputL[pos+1]] = val
 
            pos += 2

        # Imprime un valor de memoria
        elif repr[-1] == "4":

            is_rel = False
            try:
                if repr[-3] == "0":
                    res = inputL[inputL[pos+1]]
                elif repr[-3] == "1":
                    res = inputL[pos+1]
                elif repr[-3] == "2":
                    is_rel = True
                    res = inputL[inputL[pos+1]+despl_rel]
            except IndexError:
                try:
                    if is_rel:
                        res = inputL[inputL[pos+1]+despl_rel]
                    else:
                        res = inputL[inputL[pos+1]]
                except IndexError:
                    if is_rel:
                        res = mem[inputL[pos+1]+despl_rel]
                    else:
                        res = mem[inputL[pos+1]]
            
            print(res)
            pos += 2

        elif repr[-1] == "9" and len(repr) > 1 and repr[-2] == "9":
            print("Abort.")
            break
        
        elif repr[-1] == "9":

            is_rel = False
            try:
                if repr[-3] == "0":
                    val = inputL[inputL[pos+1]]
                elif repr[-3] == "1":
                    val = inputL[pos+1]
                elif repr[-3] == "2":
                    is_rel = True
                    val = inputL[inputL[pos+1]+despl_rel]
            except IndexError:
                try:
                    if is_rel:
                        val = inputL[inputL[pos+1]+despl_rel]
                    else:
                        val = inputL[inputL[pos+1]]
                except IndexError:
                    if is_rel:
                        val = mem[inputL[pos+1]+despl_rel]
                    else:
                        val = mem[inputL[pos+1]]
            
            despl_rel += val
            pos += 2

def Day9(file):

    inputL = formatInput(file)

    Intcode_computer(inputL)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d9.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day9(file)
        print("Execution time equal to {0}".format(time.time() - startTime))