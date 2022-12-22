from _collections import defaultdict

f = open("inputs/Day19.txt").read().split("\n")

beacons = set()
canSee = defaultdict(set)
canSeeAll = defaultdict(set)
posScan = dict()

scanner = 0
for line in f:
    if len(line) < 2: continue
    if line[:2] == "--":
        print(line)
        line = line.split()
        scanner = int(line[2])
    else:
        pos = tuple(map(int, line.split(",")))
        canSee[scanner].add(pos)
        canSeeAll[scanner].add(pos)

# make everything relative to scanner 0
for beacon in canSee[0]:
    beacons.add(beacon)


def r_x(pts):
    p = set()
    for pt in pts:
        pt2 = (pt[0], pt[2], -pt[1])
        p.add(pt2)

    return p


def r_y(pts):
    p = set()
    for pt in pts:
        pt2 = (-pt[2], pt[1], pt[0])
        p.add(pt2)

    return p


def r_z(pts):
    p = set()
    for pt in pts:
        pt2 = (pt[1], -pt[0], pt[2])
        p.add(pt2)

    return p

posScan[0] = (0, 0, 0)

def all_orient(pts):
    ret = []
    for x in range(4):
        for y in range(4):
            for z in range(4):
                p = set(pts)
                for i in range(x): p = r_x(p)
                for i in range(y): p = r_y(p)
                for i in range(z): p = r_z(p)
                if p not in ret:
                    ret.append(p)

    print(len(ret))
    return ret

process = [i for i in range(scanner+1)]
canSeeOrient = dict()

for i in range(1, scanner + 1):
    canSeeOrient[i] = all_orient(canSee[i])

def runloop(i):
    print("====", i, "====")
    print(len(posScan.keys()))
    for j in range(scanner + 1):
        if j in posScan: continue
#        print("==", j, "==")
        for orient in canSeeOrient[j]:
#            print(orient)
            for a in canSee[i]:
                for b in orient:
                    # assume these 2 beacons are the same
                    share = 0
                    dpos = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
                    for c in canSee[i]:
                        pos = (c[0] + dpos[0], c[1] + dpos[1], c[2] + dpos[2])
                        if pos in orient:
                            share += 1
                    if share == 12:
                        posScan[j] = (a[0] - b[0], a[1] - b[1], a[2] - b[2])
                        pts = set()
                        for b in orient:
                            pos = (b[0] - dpos[0], b[1] - dpos[1], b[2] - dpos[2])
                            pts.add(pos)
#                        print(j, pts)
                        canSee[j] = pts
                        runloop(j)
                        break
                if j in posScan:
                    break
            if j in posScan:
                break

def run():
    runloop(0)
    print(posScan)

    pts = set()
    for i in range(scanner+1):
        for item in canSee[i]:
            pts.add(item)
    print("Part 1:", len(pts))

    ans = 0
    for a in range(scanner + 1):
        for b in range(a):
            A = posScan[a]
            B = posScan[b]
            d = abs(A[0] - B[0]) + abs(A[1] - B[1]) + abs(A[2] - B[2])
            ans = max(d, ans)
    print("Part 2:", ans)


run()


