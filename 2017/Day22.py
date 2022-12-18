f = open("Day22.txt")
board = f.read().split("\n")
pos = ()
d = 0
inf = set()
tot = 0

for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] == "#": inf.add((x,y))

pos = (len(board[0]) // 2, len(board) // 2)

m = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def burst():
    global pos, d, tot
    # rotate
    if pos in inf: d += 1
    else: d -= 1

    if d >= 4: d -= 4
    elif d < 0: d += 4

    # flip
    if pos in inf:
        inf.remove(pos)
    else:
        inf.add(pos)
        tot += 1

    # move
    pos = (pos[0] + m[d][0], pos[1] + m[d][1])

n = 10000
for i in range(n):
    burst()

print("Part 1:", tot)


