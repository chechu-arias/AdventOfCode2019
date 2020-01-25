#!/usr/bin/python3

import time
import sys
import itertools

class Moon:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.speed_x = 0
        self.speed_y = 0
        self.speed_z = 0

def formatInput(file):
    moons = list()
    with open(file, "r") as data:
        for line in data:
            vals = line.replace("<","").replace(">","").replace("\n","").split(", ")
            m = Moon(int(vals[0][2:]), int(vals[1][2:]), int(vals[2][2:]))
            moons.append(m)
    return moons

def part1(moons):

    for iter in range(1000):
        for moon in moons:
            for comp_moon in moons:
                if moon != comp_moon:
                    if moon.x < comp_moon.x:
                        moon.speed_x += 1
                    elif moon.x > comp_moon.x:
                        moon.speed_x -= 1

                    if moon.y < comp_moon.y:
                        moon.speed_y += 1
                    elif moon.y > comp_moon.y:
                        moon.speed_y -= 1

                    if moon.z < comp_moon.z:
                        moon.speed_z += 1
                    elif moon.z > comp_moon.z:
                        moon.speed_z -= 1
        
        for moon in moons:
            moon.x += moon.speed_x
            moon.y += moon.speed_y
            moon.z += moon.speed_z

    return sum([ (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.speed_x) + abs(m.speed_y) + abs(m.speed_z)) for m in moons])

def calc_rep(moons, i):

    ant = set()
    indic = 0
    while True:
        for moon in moons:
            for comp_moon in moons:
                if moon != comp_moon:
                    if i == 0:
                        eje = moon.x
                        comp_eje = comp_moon.x
                    elif i == 1:
                        eje = moon.y
                        comp_eje = comp_moon.y
                    elif i == 2:
                        eje = moon.z
                        comp_eje = comp_moon.z
                    
                    if eje < comp_eje:
                            if i == 0:
                                moon.speed_x += 1
                            elif i == 1:
                                moon.speed_y += 1
                            elif i == 2:
                                moon.speed_z += 1
                    elif eje > comp_eje:
                            if i == 0:
                                moon.speed_x -= 1
                            elif i == 1:
                                moon.speed_y -= 1
                            elif i == 2:
                                moon.speed_z -= 1
        
        aux = ""
        for pos, m in enumerate(moons):
            if i == 0:
                m.x += m.speed_x
                val = str(m.x) + "," + str(m.speed_x)
            elif i == 1:
                m.y += m.speed_y
                val = str(m.y) + "," + str(m.speed_y)
            elif i == 2:
                m.z += m.speed_z
                val = str(m.z) + "," + str(m.speed_z)     

            if pos != len(moons)-1:
                aux += val + ","
            else:
                aux += val
        
        if aux in ant:
            print(indic,aux)
            break
        else:
            ant.add(aux)
        indic += 1

    return indic

def part2(moons):

    vals = [0]*3
    for i in range(3):
        vals[i] = calc_rep(moons,i)

    aux = (vals[0] * vals[1]) // gcd(vals[0], vals[1])
    return (aux * vals[2]) // gcd(aux, vals[2])

def gcd(x,y):
    while y != 0:
        new_x = y
        new_y = x % y
        x = new_x
        y = new_y
    return x

def Day12(file):

    moons = formatInput(file)
    print("Part 1 is {0}".format(part1(moons)))
    moons = formatInput(file)
    print("Part 2 is {0}".format(part2(moons)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 d9.py inputpath")
    else:
        file = sys.argv[1]
        startTime = time.time()
        Day12(file)
        print("Execution time equal to {0}".format(time.time() - startTime))