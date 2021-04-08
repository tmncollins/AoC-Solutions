
with open("input/10.txt") as f:
    mapp = f.readlines()

points = set()
asteroids = set()

for y in range(len(mapp)):
    for x in range(len(mapp[y]) - 1):
        points.add((x,y))
        if mapp[y][x] == "#":asteroids.add((x,y))

x = len(mapp[0])
y = len(mapp)

gradient = set()
angles = set()
for Y in range(y):
    for X in range(x):
        try:
            g = X / Y
        except:
            g = float("inf")
        if g not in gradient:
            angles.add((X,Y))
            angles.add((-X,Y))
            angles.add((X,-Y))
            angles.add((-X,-Y))
            gradient.add(g)
angles.add((1, 0))
angles.add((-1, 0))
#print(angles)
angles.remove((0,0))

maxa = 0
maxast = 0
for a in asteroids:
    found = set()
    for angle in angles:
        l = tuple(a)
        while l in points:
            l = (l[0] + angle[0], l[1] + angle[1])
            if l in asteroids:
                found.add(l)
                break
#    print(a, found)
    found = len(found)
    if found > maxa:
        maxa = found
        maxast = a
print(maxast, maxa)