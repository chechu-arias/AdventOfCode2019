#!/usr/bin/python3

import time
import sys

def Day3(input, part):

    vals = input.split("-")
    min = int(vals[0])
    max = int(vals[1])
    res = list()

    for num in range(min, max+1):
        repr = str(num)
        cont = 1
        cond_adjacent = False
        cond_ord = True
        for pos in range(len(repr)-1):
            if int(repr[pos]) > int(repr[pos+1]):
                cond_ord = False
            if int(repr[pos]) == int(repr[pos+1]):
                if part == 1:
                    cond_adjacent = True
                else:
                    cont += 1
            elif part == 2:
                if cont == 2:
                    cond_adjacent = True
                elif cont > 2:
                    cont = 1
            if cont == 2 and pos == len(repr)-2 and int(repr[pos+1]) == int(repr[pos]):
                cond_adjacent = True

        if cond_ord and not cond_adjacent:
            #print(num)
            pass
        if cond_adjacent and cond_ord:
            #print(num)
            res.append(repr)

    print("The number of possible passwords for part 1 is {0}".format(len(res)))




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d4.py part{1|2}")
    else:
        part = int(sys.argv[1])
        input = "248345-746315"
        startTime = time.time()
        Day3(input, part)
        print("Execution time equal to {0}".format(time.time() - startTime))