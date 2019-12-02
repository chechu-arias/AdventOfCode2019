res = 0
aux = 0
with open("inputd1.txt","r") as input:
    for line in input:
        mass = int(line)
        fuel = mass//3 - 2
        res += fuel
        while ((fuel//3)-2) > 0:
            fuel = ((fuel//3)-2)
            aux += fuel
print(res)
print(aux)
print(res+aux)
print("---------------")