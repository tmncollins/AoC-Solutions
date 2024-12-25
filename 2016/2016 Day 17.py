from collections import deque
from hashlib import md5

valid = set()

for y in range(4):
    for x in range(4):
        valid.add((x,y))

pzl_inp = input("Enter puzzle input:    ").strip()

def bfs(inp):

    pos = (0, 0)
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    text = "UDLR"
    open_hash = "bcdef"

    q = deque()
    q.append((pos, ""))
    seen = set()
    part1 = False
    part2 = 0

    while q:
        u, path = q.popleft()

        if u == (3,3):
            if not part1:
                part1 = True
                print("Part 1:", path)
            else:
                part2 = max(part2, len(path))
            continue

        hash = md5((inp + path).encode()).hexdigest()

        for i in range(4):
            if hash[i] in open_hash:
                v = (u[0] + move[i][0], u[1] + move[i][1])
                if v in valid:
                    q.append((v, path + text[i]))

    print("Part 2:", part2)

bfs(pzl_inp)

# DRURDRUDDLLDLUURRDULRLDUUDDDRR
# DRURDRUDDRDL