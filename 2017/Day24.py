from collections import *

ports = defaultdict(set)
best = defaultdict(int)
part1 = 0
part2 = (0, 0)

def bridges(l, s, used, u):
    global ports, part1, part2

    if l > part2[0]:
        part2 = (l, s)
    elif l == part2[0] and s > part2[1]:
        part2 = (l, s)

    for v in ports[u]:
        n = (min(u,v), max(u,v))
        if n not in used:
            # save length and strength of out bridge
            part1 = max(part1, s+u+v)
            used2 = set(used)
            used2.add(n)
            bridges(l+1, s+u+v, used2, v)

f = open("Day24.txt").read().split("\n")

for line in f:
    p = list(map(int, line.split("/")))
    if p[1] in ports[p[0]]: print("1")
    ports[p[0]].add(p[1])
    ports[p[1]].add(p[0])

bridges(0, 0, set(), 0)

print("Part 1:", part1)
print("Part 2:", part2[1])
