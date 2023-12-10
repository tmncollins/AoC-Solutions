from _collections import *
from heapq import *

mapp = open("inputs/Day24.txt").read().split("\n")
nums = list("0123456789")
pos = dict()
graph = set()
maxNum = 0
for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        a = mapp[y][x]
        if a in nums:
            pos[int(a)] = (x,y)
            pos[(x,y)] = int(a)
            maxNum = max(maxNum, int(a))
            graph.add((x,y))
        elif a == ".":
            graph.add((x,y))

#print(graph)
#print(pos)

INF = float("inf")
dist = [[INF for i in range(8)] for j in range(8)]
move = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(maxNum+1):
    q = deque()
    q.append((0, pos[i]))
    seen = {pos[i]}
    while q:
        d, u = q.popleft()
#        print(u)
        if u in pos:
            dist[i][pos[u]] = d
            dist[pos[u]][i] = d
        for m in move:
            v = (m[0] + u[0], m[1] + u[1])
            if v in graph and v not in seen:
                seen.add(v)
                q.append((d+1, v))

#print(dist)

q = [(0, {0}, 0)]

while q:
    d, visited, u = heappop(q)
    if len(visited) == maxNum + 1:
        print("Part 1:", d)
        break
    for i in range(maxNum+1):
        if i not in visited:
            v2 = set(visited)
            v2.add(i)
            heappush(q, (d + dist[i][u], v2, i))

q = [(0, {0}, 0)]

while q:
    d, visited, u = heappop(q)
    if len(visited) == maxNum + 1:
        if u == 0:
            print("Part 2:", d)
            break
        heappush(q, (d + dist[0][u], visited, 0))
        continue
    for i in range(maxNum+1):
        if i not in visited:
            v2 = set(visited)
            v2.add(i)
            heappush(q, (d + dist[i][u], v2, i))




