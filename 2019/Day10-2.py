
with open("input/10.txt") as f:
    mapp = f.readlines()

# station
a = (30, 34)

points = set()
asteroids = set()

for y in range(len(mapp)):
    for x in range(len(mapp[y]) - 1):
        points.add((x, y))
        if mapp[y][x] == "#": asteroids.add((x, y))

x = len(mapp[0])
y = len(mapp)

from math import *

gradient = set()
angles = set()
for Y in range(y):
    for X in range(x):
        try:
            g = X / Y
        except:
            g = 0
        an = degrees(atan(g))
        if g not in gradient:
            angles.add((an, X, -Y))
            angles.add((180 - an, X, Y))
            angles.add((180 + an, -X, Y))
            angles.add((360 - an, -X, -Y))
            gradient.add(g)
# print(angles)
angles.remove((0, 0, 0))
angles.remove((360, 0, 0))
angles.remove((180, 0, 0))
angles.add((90, 1, 0))
angles.add((270, -1, 0))
angles.add((0, 0, -1))
angles.add((180, 0, 1))
# angles.add()
angles = sorted(list(angles))
print(angles[:10])

maxa = 0
maxast = 0
shot = 0

while shot < 200:
    found = set()
    for angle in angles:
        l = tuple(a)
        while l in points:
            l = (l[0] + angle[1], l[1] + angle[2])
            if l in asteroids:
                shot += 1
                asteroids.remove(l)
                if shot <= 200:
                    print("shot:", shot, l, l[0] * 100 + l[1])
                break

    #    print(a, found)
    found = len(found)
    if found > maxa:
        maxa = found
        maxast = a
print(maxast, maxa)