from _collections import defaultdict

black = defaultdict(bool)

with open("inputs/24.txt") as f:
    contents = f.readlines()

for line in contents:
    line = line.replace("\n", "")
    index = 0
    pos = [0,0]
    while index < len(line):
        if line[index] == "e":
            pos[0] += 1
        elif line[index] == "w":
            pos[0] -= 1
        elif line[index] == "s":
            index += 1
            pos[1] += 1
            if line[index] == "e":
                pos[0] += 0.5
            elif line[index] == "w":
                pos[0] -= 0.5
        elif line[index] == "n":
            pos[1] -= 1
            index += 1
            if line[index] == "e":
                pos[0] += 0.5
            elif line[index] == "w":
                pos[0] -= 0.5
        index += 1
    black[tuple(pos)] = not black[tuple(pos)]

bl = set()
white = set()

for item in black.keys():
    if black[item]: bl.add(item)

dir = [(1,0), (-1,0), (0.5,1), (-0.5,1), (0.5,-1), (-0.5,-1)]

def getAround(point):
    around = {(point[0] + d[0], point[1] + d[1]) for d in dir}
    return around

for k in range(100):
    white = set()
    for item in bl:
        white = white.union(getAround(item))
    white = white.difference(bl)

    toRemove = set()
    for item in bl:
        c = 0
        for i in getAround(item):
            if i in bl:
                c += 1
        if c == 0 or c > 2:
            toRemove.add(item)
    toAdd = set()
    for item in white:
        c = 0
        for i in getAround(item):
            if i in bl:
                c += 1
        if c == 2:
            toAdd.add(item)

    for item in toRemove:
        bl.remove(item)
    for item in toAdd:
        bl.add(item)

    print(k, len(bl))
