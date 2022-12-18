with open("inputs/12.txt") as f:
    all_data = f.read().split("\n")

graph = dict()

for line in all_data:
    if len(line) < 5: continue
    u, vs = line.split("<->")
    vs = list(map(int, vs.split(",")))
    u = int(u)

    graph[u] = vs

seen = set()
groups = 0

for i in range(max(graph)):

    if i in seen: continue

    size = 0
    seen.add(i)
    u = i
    q = [u]
    groups += 1

    while q:
        u = q.pop()
        size += 1

        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)

    if i == 0:
        print("Part 1:", size)

print("Part 2:", groups)


