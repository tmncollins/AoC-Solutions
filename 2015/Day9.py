from _collections import *

with open("inputs/Day9.txt") as f:
    all_data = f.read().split("\n")

dist = dict()
places = set()

for line in all_data:
    if len(line) < 5: continue

    line = line.split()
    a = line[0]
    b = line[2]
    x = int(line[4])

    dist[(a,b)] = x
    dist[(b,a)] = x
    places.add(a)
    places.add(b)

for place in places:
    dist[("", place)] = 0

q = deque()
q.append((0, "", set()))
shortest = float("inf")
longest = 0

while q:
    d, u, seen = q.pop()

    if seen == places:
        shortest = min(shortest, d)
        longest = max(longest, d)
        continue

    for v in places:
        if v not in seen:
            seen2 = set(seen)
            seen2.add(v)
            q.append((d + dist[(u, v)], v, seen2))

print("Part 1:", shortest)
print("Part 2:", longest)
