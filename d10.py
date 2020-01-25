#!/usr/bin/python3

import operator
import time
import sys

def formatData(file):
    res = dict()
    input = list()
    with open(file,"r") as filedata:
        y = 0
        for line in filedata:
            x = 0
            input.append(line.split("\n"))
            for elem in line:
                if elem == "#":
                    res[(x,y)] = 0
                x += 1
            y += 1

    return res #input, res

def min(val1, val2):
    if val1 < val2:
        return val1
    else:
        return val2

def max_com_div(val1,val2):
    res = -1
    for div in range(2,min(val1,val2)+1):
        if val1%div == 0 and val2%div == 0:
            res = div
    return res

def Day10(file):

    asteroids = formatData(file)

    for pos in asteroids.keys():
        x_pos = pos[0]
        y_pos = pos[1]
        for pos_compare in asteroids.keys():
            x_comp = abs(pos_compare[0] - x_pos)
            y_comp = abs(pos_compare[1] - y_pos)
            if x_pos == 6 and y_pos == 3:
                print(pos_compare[0],pos_compare[1],asteroids[pos])
            if x_comp == 0 and y_comp == 0:
                continue
            min_v = min(x_comp,y_comp)
            if min_v == 1:
                asteroids[pos] += 1
            elif min_v == 0:

                #Misma columna
                if x_comp == 0:
                    blocked = False
                    if y_pos > pos_compare[1]:
                        for same_x in range(pos_compare[1]+1,y_pos):
                            if type(asteroids.get((x_pos,same_x),False)) != bool:
                                blocked = True
                                break
                        if not blocked:
                            asteroids[pos] += 1
                    else:
                        for same_x in range(y_pos+1,pos_compare[1]):
                            if type(asteroids.get((x_pos,same_x),False)) != bool:
                                blocked = True
                                break
                        if not blocked:
                            asteroids[pos] += 1
                #Misma fila
                else:
                    blocked = False
                    if x_pos > pos_compare[0]:
                        for same_y in range(pos_compare[0]+1,x_pos):
                            if type(asteroids.get((same_y,y_pos),False)) != bool:
                                blocked = True
                                break
                        if not blocked:
                            asteroids[pos] += 1
                    else:
                        for same_y in range(x_pos+1,pos_compare[0]):
                            if type(asteroids.get((same_y,y_pos),False)) != bool:
                                blocked = True
                                break
                        if not blocked:
                            asteroids[pos] += 1
            else:
                entr = False
                for div in range(2,min_v+1):
                    if x_comp%div==0 and y_comp%div==0:
                        entr = True
                        blocked = False
                        fact_x = x_comp//div
                        fact_y = y_comp//div
                        derecha = False
                        if x_pos > pos_compare[0]:
                            derecha = True
                        abajo = False
                        if y_pos > pos_compare[1]:
                            abajo = True
                        inv = False
                        if abajo and derecha:
                            posib_x = pos_compare[0] + fact_x
                            posib_y = pos_compare[1] + fact_y
                        elif abajo and not derecha:
                            inv = True
                            posib_x = x_pos + fact_x
                            posib_y = y_pos + fact_y
                        elif not abajo and derecha:
                            inv = True
                            posib_x = pos_compare[0] + fact_x
                            posib_y = pos_compare[1] + fact_y
                        elif not abajo and not derecha:
                            posib_x = x_pos + fact_x
                            posib_y = y_pos + fact_y
                        max_div = max_com_div(x_comp,y_comp)
                        if max_div != -1:
                            for posib_block in range(max_div-1):
                                if inv:
                                    posib_y -= 2*fact_y
                                if x_pos == 6 and y_pos == 3 and pos_compare[0] == 0 and pos_compare[1] == 7:
                                    print("---",posib_x,posib_y)
                                if type(asteroids.get((posib_x,posib_y),False)) != bool:
                                    blocked = True
                                    break
                                posib_x += fact_x
                                posib_y += fact_y
                        else:
                            for posib_block in range(min(x_comp,y_comp)-1):
                                if inv:
                                    posib_y -= 2*fact_y
                                if x_pos == 6 and y_pos == 3 and pos_compare[0] == 0 and pos_compare[1] == 7:
                                    print("---",posib_x,posib_y)
                                if type(asteroids.get((posib_x,posib_y),False)) != bool:
                                    blocked = True
                                    break
                                posib_x += fact_x
                                posib_y += fact_y
                        if not blocked:
                            asteroids[pos] += 1
                            break
                if not entr:
                    asteroids[pos] += 1
    
    max_pos = max(asteroids.items(), key=operator.itemgetter(1))[0]
    print("La mejor posición es {0}, pudiendo ver {1} asteroides".format(max_pos, asteroids[max_pos]))





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d10.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day10(file)
        print("Execution time equal to {0}".format(time.time() - startTime))