from heapq import *
from math import *
from _collections import *
from copy import deepcopy
from itertools import *

with open("inputs/Day11.txt") as f:
    all_data = f.read().split("\n")

floors = []
floor = 0
elements = dict()
new_element = 1

# generators are positive, microchips are negative

for line in all_data:
    if len(line) < 5: continue
    line = line.replace(",", "").replace(".", "").split()

    floors.append([])

    for i in range(len(line)):
        if line[i] == "generator":
            element = line[i-1]
            if element not in elements:
                elements[element] = new_element
                new_element += 1
            floors[-1].append(elements[element])
        elif line[i] == "microchip":
            element = line[i-1].replace("-compatible", "")
            if element not in elements:
                elements[element] = new_element
                new_element += 1
            floors[-1].append(-elements[element])

    floor += 1

for floor in floors: floor.sort()


def safe(floor):
    if len(floor) == 0 or floor[-1] < 0: return True # no generators
    for i in floor:
        if i < 0:
            if -i not in floor: return False
    return True


def run(floors):

    q = [(0, 0, floors, 0)]
    seen = dict()

    while q:

        _, d, floors, e = heappop(q)

        if e == 3:
            finished = True
            for floor in range(3):
                if len(floors[floor]) > 0:
                    finished = False
                    break
            if finished:
                return d

        directions = []
        if e > 0: directions.append(-1)
        if e < 3: directions.append(1)

        moves = list(combinations(floors[e], 2)) + list(combinations(floors[e], 1))
        for dir in directions:
            for m in moves:

                new_floors = deepcopy(floors)
                new_floors[e] = []
                for item in floors[e]:
                    if item not in m:
                        new_floors[e].append(item)
                new_floors[e] = tuple(new_floors[e])
                new_floors[e+dir] = list(new_floors[e+dir])
                for item in m:
                    new_floors[e+dir].append(item)
                new_floors[e+dir].sort()
                new_floors[e+dir] = tuple(new_floors[e+dir])

                if not safe(new_floors[e]) or not safe(new_floors[e+dir]):
                    continue
                        



