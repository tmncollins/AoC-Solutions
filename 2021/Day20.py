from _collections import defaultdict

f = open("Day20.txt").read().split("\n")

algorithm = list(map(int, list(f[0].replace(".", "0").replace("#", "1"))))

# 0 for dark, 1 for light
img = defaultdict(int)

da = 1

minX = -da
minY = 2 - da
maxX = 0
maxY = 0

for y in range(2, len(f)):
    maxY = max(maxY, y+da)
    for x in range(len(f[y])):
        maxX = max(maxX, x+da)
        if f[y][x] == "#":
            img[(x,y)] = 1
        else:
            img[(x,y)] = 0

MINX = 0
MINY = 2
MAXX = maxX - da
MAXY = maxY - da

directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]

def enhance(img, minX, minY, maxX, maxY, outer = 0):

    output = dict()

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            nums = ""
            for d in directions:
                if (x + d[0], y + d[1]) in img:
                    nums += str(img[(x + d[0], y + d[1])])
                else:
                    nums += outer
            v = int(nums, 2)
#            print(v)
            output[(x,y)] = algorithm[v]

    return output

def output(img, minX, minY, maxX, maxY):
    for y in range(minY, maxY + 1):
        line = ""
        for x in range(minX, maxX + 1):
            line += "#" if (x,y) in img and img[(x,y)] == 1 else "."
        print(line)
    print()

def count(img, minX, minY, maxX, maxY):
    v = 0
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if img[(x,y)] == 1:
                v += 1
    return v

#output(img, minX, minY, maxX, maxY)

outer = 0
n = 50
for i in range(n):
    j = i+1
    img = enhance(img, minX, minY, maxX, maxY, str(outer))
#    output(img, minX, minY, maxX, maxY)
    if j == 2:
        print("Part 1:", count(img, MINX - j, MINY - j, MAXX + j, MAXY + j))
    elif j == 50:
        print("Part 2:", count(img, MINX - j, MINY - j, MAXX + j, MAXY + j))

    minY, minX = minY - da, minX - da
    maxY, maxX = maxY + da, maxX + da
    if outer == 0:
        outer = algorithm[0]
    else:
        outer = algorithm[-1]
