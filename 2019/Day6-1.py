from collections import defaultdict

with open("input/6.txt") as f:
    data = f.readlines()

graph = defaultdict(list)
graphB = defaultdict(list)
nodes = set()

for line in data:
    line = line.replace("\n", "")
    line = line.split(")")
    graph[line[0]].append(line[1])
    graphB[line[1]].append(line[0])
    nodes.add(line[0])
    nodes.add(line[1])

start = "COM"
seen = set()
counter = {"COM":0}
pending = [start]

while len(seen) < len(nodes) and len(pending) > 0:
    look = pending.pop()
    next = graph[look]
    seen.add(look)
    for item in next:
        if item not in seen:
            counter[item] = counter[look] + 1
            pending.append(item)

print(counter)
print(sum(counter.values()))