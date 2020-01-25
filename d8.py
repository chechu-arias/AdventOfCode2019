#!/usr/bin/python3

import time
import sys

def Day8(file):
    wide = 25
    tall = 6
    layer_elems = wide*tall
    cont = 0

    #wide_cont = 0
    #tall_cont = 0
    #wide_sep = list()
    #layer = list()

    layers = list()
    aux = list()
    
    with open(file,"r") as filedata:
        for line in filedata:
            for elem in line:
                aux.append(elem)
                cont += 1
                if cont == layer_elems:
                    layers.append(aux)
                    cont = 0
                    aux = list()

    pos_0, min_0 = -1, 0
    for pos in range(len(layers)):
        if pos_0 == -1:
            pos_0, min_0 = pos, layers[pos].count('0')
        elif layers[pos].count('0') < min_0:
            pos_0, min_0 = pos, layers[pos].count('0')

    print(pos_0, min_0)
    part1 = layers[pos_0].count('1')*layers[pos_0].count('2')
    print("Part 1 is {0}".format(part1))

    part2 = list()
    layer_ind = list()
    for i in range(wide*tall):
        for pos in range(len(layers)):
            if layers[pos][i] == '0' or layers[pos][i] == '1':
                part2.append(layers[pos][i])
                layer_ind.append(pos)
                break
    
    part2 = str(part2).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ","")
    part2 = part2.replace('0',' ').replace('1','@')

    print("Part 2 is: ")
    for i in range(tall):
        print(part2[i*wide:(i+1)*wide])

        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d8.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day8(file)
        print("Execution time equal to {0}".format(time.time() - startTime))