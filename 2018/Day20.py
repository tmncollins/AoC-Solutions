from _collections import defaultdict, deque

with open("input/20.txt") as f:
    regex = f.read().strip("\n ^$")

start = (0, 0)
graph = defaultdict(set)


def output(minx, maxx, miny, maxy):
    for y in range(miny, maxy + 1):
        line = ["", ""]
        for x in range(minx, maxx + 1):

            if len(graph[(x,y)]) > 0: line[0] += "."
            else: line[0] += "#"

            if (x+1,y) in graph[(x,y)]: line[0] += "."
            else: line[0] += "#"
            if (x,y+1) in graph[(x,y)]: line[1] += "."
            else: line[1] += "#"
            line[1] += "#"

        for l in line:
            print(l)


def update_pos(pos, char):
    if char == "N":
        return (pos[0], pos[1] - 1)
    elif char == "S":
        return (pos[0], pos[1] + 1)
    elif char == "E":
        return (pos[0] + 1, pos[1])
    elif char == "W":
        return (pos[0] - 1, pos[1])


positions = {(0, 0)}
restart_pos = {(0, 0)}
end_pos = set()
nested = []

for char in regex:

    if char == "|":
        # restart from last fork
        for pos in positions:
            end_pos.add(pos)
        positions = restart_pos

    elif char == "(":
        # start nested forks
        nested.append((restart_pos, end_pos))
        restart_pos = positions
        end_pos = set()

    elif char == ")":
        # finished nested fork
        for pos in end_pos:
            positions.add(pos)
        # grab info stored in nested
        restart_pos, end_pos = nested.pop()

    else:
        new_pos = set()
        for pos in positions:
            npos = update_pos(pos, char)
            graph[pos].add(npos)
            graph[npos].add(pos)
            new_pos.add(npos)
        positions = new_pos

#print(graph)

q = deque()
q.append(((0,0), 0))
seen = {(0,0)}

max_d = 0
part2 = 0

while q:
    u, d = q.popleft()
    max_d = max(max_d, d)

    if d >= 1000:
        part2 += 1

    for v in graph[u]:
        if v not in seen:
            seen.add(v)
            q.append((v, d+1))

print("Part 1:", max_d)
print("Part 2:", part2)
