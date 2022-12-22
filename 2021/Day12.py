from _collections import defaultdict, deque

data = open("inputs/Day12.txt").read().split("\n")
lower = "abcdefghijklmnopqrstuvwxyz"
lower = set(lower)
lower.add("start")

graph = defaultdict(set)

for item in data:
    a,b = item.split("-")
    graph[a].add(b)
    graph[b].add(a)

q = deque()
q.append(("start", {"start"}))

paths = 0
while q:
    u, seen = q.popleft()
#    print(seen, u)

    if u == "end":
        paths += 1
        continue

    for v in graph[u]:
        if v == v.lower() and v in seen:
            pass
        else:
            s2 = set(seen)
            s2.add(v)
            q.append((v, s2))


print("Part 1:", paths)

q = deque()
q.append(("start", {"start"}, False))

paths = 0

while q:
    u, seen, small = q.popleft()

    if u == "end":
        paths += 1
        continue

    for v in graph[u]:
        if v == "start":
            continue
        if v == v.lower() and v in seen:
            if small:
                continue
            s2 = set(seen)
            q.append((v, s2, True))
        else:
            s2 = set(seen)
            s2.add(v)
            q.append((v, s2, small))

print("Part 2:", paths)