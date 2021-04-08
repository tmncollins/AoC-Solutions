from math import *

from collections import defaultdict

with open("input/14.txt") as f:
    craft = f.readlines()

oreFuse = dict()
graph = dict()
quant = dict()
reverse = defaultdict(list)
for item in craft:
    item = item.replace("\n", "")
    item = item.split("=>")
    pro = item[1]
    ing = item[0]
    ings = ing.split(",")
    for i in range(len(ings)):
        ings[i] = ings[i].split()
    graph[pro.split()[1]] = ings
    quant[pro.split()[1]] = int(pro.split()[0])
    if ings[0][1] == "ORE":
        oreFuse[pro.split()[1]] = (pro.split()[0], ings[0][0])

    for item in ings:
        reverse[item[1]].append(pro.split()[1])



def ore_for_fuel(nFuel):
    req = {"FUEL": nFuel}

    pending = ["FUEL"]
    print(req)
    while len(pending) > 0:
        for item in pending:
            q = quant[item]
            ingreds = graph[item]
            mult = (req[item] + q - 1) // q
            for (ingQ, ing) in ingreds:
                v = mult * int(ingQ)
                if ing in req.keys():
                    v += req[ing]
                req[ing] = v
            req[item] -= mult * q
        pending = []
        for item in req.keys():
            if req[item] > 0 and item != "ORE":
                pending.append(item)
#        print(pending, req)

    print(req)
    return req["ORE"]

print(graph)
print(ore_for_fuel(1))


