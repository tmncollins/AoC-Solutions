from collections import defaultdict
from functools import lru_cache

with open("inputs/Day23.txt", "r") as f:
    all_data = f.read().split("\n")

graph = defaultdict(set)

t_set = set()

for line in all_data:
    if len(line) < 3: continue
    a,b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)
    if a[0] == "t": t_set.add(a)
    if b[0] == "t": t_set.add(b)

part1 = set()
for a in t_set:
    for b in graph[a]:
        for c in graph[a]:
            if b == c: continue
            if c in graph[b]:
                part1.add(tuple(sorted([a,b,c])))

@lru_cache(maxsize=None)
def maximum_clique(clique, can_add):
    global best_clique
    if len(clique) == 0: clique = set()
    else: clique = set(clique.split(","))
    can_add = set(can_add.split(","))
#    print(clique, can_add)
    if len(clique) > len(best_clique):
        best_clique = sorted(list(clique))
#        print(",".join(best_clique), len(best_clique))

    if len(can_add) == 0: return
    for item in can_add:
        connected = True
        if len(graph[item]) < len(clique):
            connected = False
        else:
            for i in clique:
                if i not in graph[item]:
                    connected = False
                    break
        if connected:
            can_add.remove(item)
            clique.add(item)
            c = ",".join(sorted(list(clique)))
            ca = ",".join(sorted(list(can_add)))
            maximum_clique(c, ca)
            can_add.add(item)
            clique.remove(item)

def max_clique(u):
    global best_clique
    best_clique = []
    maximum_clique(u, ",".join(graph[u]))
    return best_clique


best_clique = []
print("Part 1:", len(part1))

part2 = []
for item in graph:
    if len(graph[item]) <= len(part2): continue
    x = max_clique(item)
    if len(x) > len(part2):
        part2 = x
        print(",".join(sorted(part2)))
print("Part 2:", ",".join(sorted(part2)))
