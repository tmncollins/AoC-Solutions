from heapq import *
from time import time

with open("inputs/Day17.txt") as file:
    data = file.read().strip().split("\n")

def rotate90(direction, clockwise):
    if clockwise:
        return (-direction[1], direction[0])
    else:
        return (direction[1], -direction[0])


def on_board(pos):
    x, y = pos
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    return True

for i in range(len(data)):
    data[i] = list(map(int, list(data[i])))

start_time = time()

q = []
seen = dict()
s = -data[0][0]
for i in range(4):
    node = ((i, 0), (1, 0))
    s += data[0][i]
    seen[node] = s
    heappush(q, (s, node[0], node[1]))

width = len(data[2])
height = len(data)
end = (width-1, height-1)

while True:
    score, pos, direction = heappop(q)
#    print(pos, seen[(pos, direction)])

    if pos == end:
        print("Part 1:", seen[(pos, direction)])
        break

    direction1 = rotate90(direction, True)
    score1 = score
    for i in range(3):
        new_pos = (pos[0] + direction1[0] * (i+1), pos[1] + direction1[1] * (i+1))
        if on_board(new_pos):
            score1 += data[new_pos[1]][new_pos[0]]
            node = (new_pos, direction1)
            if node not in seen or score1 < seen[node]:
                seen[node] = score1
                heappush(q, (score1, new_pos, direction1))
        else:
            break

    direction2 = rotate90(direction, False)
    score2 = score
    for i in range(3):
        new_pos = (pos[0] + direction2[0] * (i+1), pos[1] + direction2[1] * (i+1))
        if on_board(new_pos):
            score2 += data[new_pos[1]][new_pos[0]]
            node = (new_pos, direction2)
            if node not in seen or score2 < seen[node]:
                seen[node] = score2
                heappush(q, (score2, new_pos, direction2))
        else:
            break

print("Time Taken:", time() - start_time)