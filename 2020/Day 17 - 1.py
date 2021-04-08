with open('inputs/17.txt', 'r') as f: #open the file
    rules = f.readlines()

from _collections import defaultdict

cubes = defaultdict(int)
dir = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1), (1,0,1), (1,0,-1), (-1,0,1),(-1,0,-1),(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]

def output(x,y,z):
    for j in range(-y,y):
        for i in range(-x, x):
            print(cubes[(j,i,z)], end="")
        print()
    print()

def getN(x,y,z):
    global cubes, dir
    tot = 0
    for d in dir:
        X,Y,Z = x+d[0], y+d[1], z+d[2]
        tot += cubes[(X,Y,Z)]
    return tot

off = len(rules) // 2
for y in range(len(rules)):
    for x in range(len(rules[0])):
        try:
            if rules[y][x] == "#":
                cubes[(x-off,y-off,0)] = 1
        except:
            pass

print(sum(cubes.values()))
cycles = 6
RANGE = 30
maxX = [-RANGE,RANGE]
maxY = [-RANGE,RANGE]
maxZ = [-RANGE,RANGE]
for i in range(cycles):
    toKill = set()
    toMake = set()
#    output(5,5,0)
    for x in range(maxX[0], maxX[1] + 1):
        for y in range(maxY[0], maxY[1] + 1):
            for z in range(maxZ[0], maxZ[1] + 1):
                if cubes[(x,y,z)] == 1:
                    n = getN(x,y,z)
                    if n not in [2,3]:
                        toKill.add((x,y,z))
                else:
                    n = getN(x,y,z)
                    if n == 3:
                        toMake.add((x,y,z))

    for item in toKill:
        cubes[item] = 0
    for x,y,z in toMake:
        if x < maxX[0]:
            maxX[0] = x
        elif x > maxX[1]:
            maxX[1] = x
        if y < maxY[0]:
            maxY[0] = y
        elif y > maxY[1]:
            maxY[1] = y
        if z < maxZ[0]:
            maxZ[0] = z
        elif z > maxZ[1]:
            maxZ[1] = z
        cubes[(x,y,z)] = 1



print(sum(cubes.values()))