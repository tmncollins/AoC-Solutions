from collections import  defaultdict

with open("input/6.txt") as f:
    data = f.readlines()

graph = defaultdict(list)
graphB = defaultdict(list)
nodes = set()
for line in data:
    line = line.replace("\n", "")
    line = line.split(")")
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])
    nodes.add(line[0])
    nodes.add(line[1])

start = "YOU"
seen = set()
pending = [(start,0)]
while len(seen) < len(nodes) and len(pending) > 0:
    look = pending.pop()
    look, d = look[0], look[1]
    if look == "SAN":
        print(d-2)
        break
    next = graph[look] + graphB[look]
    seen.add(look)
    for item in next:
        if item not in seen:
            pending.append((item,d+1))