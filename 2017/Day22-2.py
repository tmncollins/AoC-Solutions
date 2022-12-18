from _collections import defaultdict

f = open("Day22.txt")
board = f.read().split("\n")
pos = ()
d = 0
inf = defaultdict(int)
tot = 0
CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] == "#": inf[(x,y)] = INFECTED

pos = (len(board[0]) // 2, len(board) // 2)

m = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def burst():
    global pos, d, tot
    # rotate
    if inf[pos] == INFECTED: d += 1
    elif inf[pos] == CLEAN: d-= 1
    elif inf[pos] == FLAGGED: d += 2

    if d >= 4: d -= 4
    elif d < 0: d += 4

    # flip
    inf[pos] += 1
    if (inf[pos] == INFECTED): tot += 1
    if (inf[pos] >= 4): inf[pos] -= 4

    # move
    pos = (pos[0] + m[d][0], pos[1] + m[d][1])

n = 10000000
for i in range(n):
    if (i % 100000 == 0): print(i)
    burst()

print("Part 2:", tot)


