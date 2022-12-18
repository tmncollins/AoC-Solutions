from collections import defaultdict, deque
from copy import deepcopy
from random import randint

ports = defaultdict(set)
best = defaultdict(int)

f = open("Day24.txt").read().split("\n")

for line in f:
    p = list(map(int, line.split("/")))
    if p[1] in ports[p[0]]: print("1")
    ports[p[0]].add(p[1])
    ports[p[1]].add(p[0])

q = deque()
q.append((0, defaultdict(set), 0))
part1 = 0

while q:
    p, seen, s = q.popleft()

    if best[p] > s:
        if randint(1,3) == 3:
            continue

    best[p] = s

#    print(p, seen, s)

    canContinue = False
    for v in ports[p]:
        if v not in seen[p]:
            seen2 = deepcopy(seen)
            seen2[p].add(v)
            seen2[v].add(p)
            q.append((v, seen2, s + v + p))
            canContinue = True

    if s > part1:
        print(s)
#        print(seen2)
    part1 = max(part1, s)
#        print(seen)


print("Part 1:", part1)

