#!/usr/bin/python3

import time
import sys
import math

def getNum(input):
    num = ""
    with open(input,"r") as data:
        for line in data:
            num = line.replace("\n","")
    return num

def part1(num_list, next_num_list, patr):
    for iter in range(100):
        for pos in range(1,len(num_list)+1):
            aux = []
            cont_glob = 0
            patr_pos = 0
            while len(aux) != len(num_list):
                aux = aux + [patr[patr_pos]]*pos
                if cont_glob == 0:
                    aux.pop()
                patr_pos = (patr_pos+1)%len(patr)
                if len(aux) > len(num_list):
                    aux = aux[0:len(num_list)]
                cont_glob += 1
            val = 0
            for pos in range(len(num_list)):
                if num_list[pos] != 0 and aux[pos] != 0:
                    val += num_list[pos]*aux[pos]
            val = abs(val)
            if val >= 10:
                next_num_list.append(int(str(val)[-1]))
            else:
                next_num_list.append(val)
        num_list, next_num_list = next_num_list, []
        print(num_list[-6:])
    print("Part 1 is " + "".join(map(str,num_list[0:8])))

def part2(num_list, iters):
    res = num_list
    for i in range(0, iters):
        sum = 0
        for j in range(len(res) - 1, -1, -1):
            sum += res[j]
            res[j] = sum % 10
    return res

def Day16(input):

    num_list = list()
    input_num = str(getNum(input))
    
    for n in input_num:
        num_list.append(int(n))

    #part1(num_list, [], [ 0, 1, 0, -1 ])

    offset = int(input_num[:7])
    dataL = len(num_list) * 10000
    necessaryL = dataL - offset
    copies = math.ceil(necessaryL / len(num_list))

    num_list = num_list*copies
    num_list = num_list[-necessaryL:]

    res = part2(num_list, 100)
    
    print(''.join([str(d) for d in res[:8]]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d16.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day16(file)
        print("Execution time equal to {0}".format(time.time() - startTime))