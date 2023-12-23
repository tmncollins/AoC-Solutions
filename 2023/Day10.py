from _collections import deque

with open("inputs/Day10.txt") as file:
    data = file.read().strip().split("\n")

pipes = ["-", "|", "F", "7", "L", "J"]
directions = [(1,0), (0,1), (0,-1), (0,-1), (0,1), (0,1)]

def next_direction(direction, pipe):
    if pipe == "-":
        if direction in [(1,0), (-1, 0)]: return direction
        return None
    if pipe == "|":
        if direction in [(0,1), (0,-1)]: return direction
        return None
    if pipe == "F":
        if direction == (0,-1): return (1,0)
        if direction == (-1,0): return (0,1)
        return None
    if pipe == "7":
        if direction == (0,-1): return (-1,0)
        if direction == (1,0): return (0,1)
        return None
    if pipe == "L":
        if direction == (0,1): return (1,0)
        if direction == (-1,0): return (0,-1)
        return None
    if pipe == "J":
        if direction == (0,1): return (-1,0)
        if direction == (1,0): return (0,-1)
        return None

for y in range(len(data)):
    data[y] = list(data[y])
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (x, y)

def generate_loop(x, y):
    S = data[y][x]
    loop = [(x, y)]
    d = directions[pipes.index(S)]
    while True:
        d = next_direction(d, data[y][x])
        if d == None: return None
        x += d[0]
        y += d[1]
        loop.append((x, y))
        if x < 0 or y < 0: return None
        if y >= len(data) or x >= len(data[y]): return None
        if loop[-1] == loop[0]:
#            print(S, d, directions[pipes.index(S)])
            if d == directions[pipes.index(S)]:
                loop.pop()
                return loop
            return None

def count_in_loop(loop):
    w = len(data[3])
    empty = ["." for _ in range(w*2+1)]
    blown_up = [list(empty)]
    for y in range(len(data)):
        line = ["."]
        for x in range(len(data[y])):
            if (x,y) in loop:
                line.append(data[y][x])
            else: line.append(".")
            line.append(".")
        blown_up.append(line)
        blown_up.append(list(empty))

    empties = 0
    for y in range(1, len(blown_up)-1):
        for x in range(1, len(blown_up[y])-1):
            if blown_up[y][x] == ".":
                if blown_up[y][x-1] != "." and blown_up[y][x+1] != ".":
                    if blown_up[y][x-1] in "-LF" and blown_up[y][x+1] in "-J7":
                        blown_up[y][x] = "-"
                if blown_up[y-1][x] != "." and blown_up[y+1][x] != ".":
                    if blown_up[y-1][x] in "|F7" and blown_up[y+1][x] in "|JL":
                        blown_up[y][x] = "|"

    for y in range(len(blown_up)):
        for x in range(len(blown_up[y])):
            if blown_up[y][x] == ".": empties += 1

    start = (0, 0)
    q = deque()
    q.append(start)
    seen = {start}

    while len(q) > 0:
        p = q.popleft()
        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            pp = (p[0] + d[0], p[1] + d[1])
            if pp[0] >= 0 and pp[1] >= 0 and pp[0] < len(blown_up[0]) and pp[1] < len(blown_up):
                if blown_up[pp[1]][pp[0]] == ".":
                    if pp not in seen:
                        seen.add(pp)
                        q.append(pp)

    for y in range(len(blown_up)):
        for x in range(len(blown_up[y])):
            if blown_up[y][x] == "." and (x,y) not in seen:
                start = (x,y)

    q = deque()
    q.append(start)
    seen = {start}
    area = 0

    while len(q) > 0:
        p = q.popleft()

        free = True
#        for d in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        for d in [(-1,-1), (-1,0), (0,-1)]:
            dx = p[0] + d[0]
            dy = p[1] + d[1]
            if blown_up[dy][dx] != ".":
                free = False
                break
        if free: area += 1

        for d in [(-1,0), (1,0), (0,-1), (0,1)]:
            pp = (p[0] + d[0], p[1] + d[1])
            if pp[0] >= 0 and pp[1] >= 0 and pp[0] < len(blown_up[0]) and pp[1] < len(blown_up):
                if blown_up[pp[1]][pp[0]] == ".":
                    if pp not in seen:
                        seen.add(pp)
                        q.append(pp)

    return area//4

for p in pipes:
    data[start[1]][start[0]] = p
    loop = generate_loop(start[0], start[1])
    if loop != None:
        print("Part 1:", len(loop)//2)
        print("Part 2:", count_in_loop(loop))
        break