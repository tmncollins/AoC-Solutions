data = open("inputs/Day13.txt").read().split("\n")

folds = []
pts = set()

b = False
for l in data:
    if l == "":
        b = True
        continue
    if b:
        folds.append(l)
    else:
        x,y = list(map(int, l.split(",")))
        pts.add((x,y))


def foldX(x, pts):
    pts2 = set()
    for p in pts:
        if p[0] > x:
            dx = p[0] - x
            p2 = (x - dx, p[1])
            pts2.add(p2)
        else:
            pts2.add(p)
    return pts2


def foldY(y, pts):
    pts2 = set()
    for p in pts:
        if p[1] > y:
            dy = p[1] - y
            p2 = (p[0], y - dy)
            pts2.add(p2)
        else:
            pts2.add(p)
    return pts2

def output(pts):
    for y in range(10):
        l = ""
        for x in range(50):
            if (x,y) in pts:
                l += "#"
            else:
                l += " "
        print(l)

i = 0
for f in folds:
    f = f.split()
    f = f[2]
    a,b = f.split("=")
    b = int(b)
    if a == "x":
        pts = foldX(b, pts)
    else:
        pts = foldY(b, pts)
    if i == 0:
        print("Part 1:", len(pts))
    i += 1

output(pts)
