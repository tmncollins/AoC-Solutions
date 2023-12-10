from _collections import defaultdict, deque

class node:
    def __init__(self, x, y, used, free):
        self.pos = (x,y)
        self.used = used
        self.free = free

data = open("inputs/Day22.txt").read().split("\n")

nodes = []
for i in range(2, len(data)):
    line = data[i].split()
    a,x,y = line[0].split("-")
    x = int(x[1:])
    y = int(y[1:])
    used = int(line[2][:-1])
    free = int(line[3][:-1])
    n = node(x,y,used,free)
    nodes.append(n)

#print(nodes)
viable = 0
for a in range(len(nodes)):
    for b in range(len(nodes)):
        if a != b:
            if nodes[a].used > 0 and nodes[a].used <= nodes[b].free:
                viable += 1
print("Part 1:", viable)

# 0 is blocked
# 1 is moveable
# 2 is free
grid = set()

end = (0, 0)
for n in nodes:
    if n.free >= 80:
        free = n.pos
    if n.used <= 80:
        grid.add(n.pos)
    if n.pos[1] == 0 and n.pos[0] > end[0]:
        end = n.pos

"""
for y in range(-1, 26):
    a = ""
    for x in range(-1, 38):
        if (x,y) == free:
            a += "_"
        elif (x,y) == end:
            a += "G"
        elif (x,y) in grid:
            a += "."
        else:
            a += "#"
    print(a)
"""

q = deque()
q.append((0, free))
aim = (end[0]-1, end[1])
dist = 0

seen = {free}
move = [(0,1),(0,-1),(1,0),(-1,0)]
while q:
    d, u = q.popleft()
    if u == aim:
        dist = d
        break

    for m in move:
        v = (m[0] + u[0], m[1] + u[1])
        if v in grid and v not in seen:
            seen.add(v)
            q.append((d+1, v))

dist += 1
dist += 5 * aim[0]

print("Part 2:", dist)



