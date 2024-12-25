from heapq import *
from math import *
from _collections import *

with open("inputs/Day11.txt") as f:
    all_data = f.read().split("\n")


def f(floors, dist=0):
    return dist - len(floors[3])*5
    d = 0
    extra = 0
    x = 4
    for i in range(len(floors)-1):
        extra += len(floors[i]) * x
        d += extra//2
        x -= 1
    return d + dist


def hash(floors):
    h = ""
    for f in floors:
        h += "-".join(sorted(f)) + "#"
    return h


floors = []
floor = 0

for line in all_data:
    if len(line) < 5: continue
    line = line.replace(",", "").replace(".", "").split()

    floors.append(set())

    for i in range(len(line)):
        if line[i] == "generator":
            floors[-1].add("g" + line[i-1])
        elif line[i] == "microchip":
            floors[-1].add("m" + line[i-1].replace("-compatible", ""))

    floor += 1


def safe(floor):
    rtg = False
    for item in floor:
        if item[0] == "g":
            rtg = True
            break
    if not rtg: return True
    for item in floor:
        if item[0] == "m":
            type = item[1:]
            if "g" + type not in floor: return False
    return True


def run(floors):
    q = [(0, 0, floors, 0)]
    seen = defaultdict(int)

    last_d = 0
    while q:

        x, d, u, e = heappop(q)
        if d > last_d:
            print(d)
            last_d = d

        if e == len(u)-1:
            end = True
            for i in range(len(u)-1):
                if len(u[i]) != 0:
                    end = False
                    break
            if end:
                print("got:", d)
#                continue
                return d

        # move up
        fl = list(u[e])
        if e < len(u)-1:
            can_two = False
            for i in range(len(fl)+1):
                if i == len(fl):
                    item1 = ""
                    if can_two: break
                else:
                    item1 = fl[i]

                for j in range(i):
                    item2 = fl[j]

                    floor = set(u[e])
                    floor.remove(item2)
                    if item1 != "": floor.remove(item1)

                    floor_above = set(u[e+1])
                    if item1 != "": floor_above.add(item1)
                    floor_above.add(item2)

                    if safe(floor_above) and safe(floor):
                        # add to q
                        v = [set(u[i]) for i in range(len(u))]
                        v[e] = floor
                        v[e+1] = floor_above

                        v_hash = hash(v) + str(e+1)
                        can_two = True
                        if seen[v_hash] == 0 or d+1 < seen[v_hash]:
                            seen[v_hash] = d+1
                            heappush(q, (f(v, d+1), d+1, v, e+1))

        # move down
        move_down = False
        for i in range(e):
            if len(u[e]) > 0:
                move_down = True
            break
        if not move_down:
            continue

        fl = list(u[e])
        if e > 0:
            for i in range(len(fl) + 1):
                if i == len(fl):
                    item1 = ""
                else:
                    item1 = fl[i]
                for j in range(i):
                    item2 = fl[j]

                    floor = set(u[e])
                    floor.remove(item2)
                    if item1 != "": floor.remove(item1)

                    floor_below = set(u[e-1])
                    if item1 != "": floor_below.add(item1)
                    floor_below.add(item2)

                    if safe(floor_below) and safe(floor):
                        # add to q
                        v = [set(u[i]) for i in range(len(u))]
                        v[e] = floor
                        v[e - 1] = floor_below

                        v_hash = hash(v) + str(e-1)
                        if seen[v_hash] == 0 or d + 1 < seen[v_hash]:
                            seen[v_hash] = d + 1
                            heappush(q, (f(v, d+1), d+1, v, e-1))


print("Part 1:", run(list(floors)))

fl = list(floors)
part2 = ["gelerium", "melerium", "gdilithium", "mdilithium"]
for x in part2:
    fl[0].add(x)

print("Part 2:", run(fl))