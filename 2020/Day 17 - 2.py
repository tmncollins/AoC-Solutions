with open('inputs/17.txt', 'r') as f: #open the file
    rules = f.readlines()

from _collections import defaultdict

cubes = defaultdict(int)
dir = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,1,1), (0,1,-1), (0,-1,1), (0,-1,-1), (1,0,1), (1,0,-1), (-1,0,1),(-1,0,-1),(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]
dir = [-1,0,1]

def output(x,y,z):
    for j in range(-y,y):
        for i in range(-x, x):
            print(cubes[(j,i,z)], end="")
        print()
    print()

def getN(x,y,z,w):
    global cubes, dir
    tot = 0
    for dX in dir:
        for dY in dir:
            for dZ in dir:
                for dW in dir:
                    X,Y,Z,W = x+dX, y+dY, z+dZ, w+dW
                    if (X,Y,Z,W) != (x,y,z,w):
                        tot += cubes[(X,Y,Z,W)]
    return tot

off = len(rules) // 2
for y in range(len(rules)):
    for x in range(len(rules[0])):
        try:
            if rules[y][x] == "#":
                cubes[(x-off,y-off,0,0)] = 1
        except:
            pass

print(sum(cubes.values()))
cycles = 6
RANGE = 5
maxX = [-RANGE,RANGE]
maxY = [-RANGE,RANGE]
maxZ = [-RANGE,RANGE]
maxW = [-RANGE,RANGE]
for i in range(cycles):
    toKill = set()
    toMake = set()
#    output(5,5,0)
    for x in range(maxX[0], maxX[1] + 1):
        for y in range(maxY[0], maxY[1] + 1):
            for z in range(maxZ[0], maxZ[1] + 1):
                for w in range(maxW[0], maxW[1] + 1):
                    if cubes[(x,y,z,w)] == 1:
                        n = getN(x,y,z,w)
                        if n not in [2,3]:
                            toKill.add((x,y,z,w))
                    else:
                        n = getN(x,y,z,w)
                        if n == 3:
                            toMake.add((x,y,z,w))

    for item in toKill:
        cubes[item] = 0
    off = 2
    for x,y,z,w in toMake:
        if x <= maxX[0]:
            maxX[0] = x-off
        elif x >= maxX[1]:
            maxX[1] = x+off
        if y <= maxY[0]:
            maxY[0] = y-off
        elif y >= maxY[1]:
            maxY[1] = y+off
        if z <= maxZ[0]:
            maxZ[0] = z-off
        elif z >= maxZ[1]:
            maxZ[1] = z+off
        if w <= maxW[0]:
            maxW[0] = w-off
        elif w >= maxW[1]:
            maxW[1] = w+off
        cubes[(x,y,z,w)] = 1

    print(sum(cubes.values()))

print(sum(cubes.values()))