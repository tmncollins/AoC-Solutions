import time

with open("inputs/Day9.txt") as f:
    all_data = f.read().split("\n")

dir = {"U": (0, -1), "R": (1, 0), "L":(-1, 0), "D":(0, 1)}


def update_tail(head, tail):
    if head == (tail[0]+2, tail[1]):
        tail = (tail[0]+1, tail[1])
    elif head == (tail[0]-2, tail[1]):
        tail = (tail[0]-1, tail[1])
    elif head == (tail[0], tail[1]+2):
        tail = (tail[0], tail[1]+1)
    elif head == (tail[0], tail[1]-2):
        tail = (tail[0], tail[1]-1)

    elif head == (tail[0]+1, tail[1]+2):
        tail = (tail[0]+1, tail[1]+1)
    elif head == (tail[0]+1, tail[1]-2):
        tail = (tail[0]+1, tail[1]-1)
    elif head == (tail[0] - 1, tail[1] + 2):
        tail = (tail[0] - 1, tail[1] + 1)
    elif head == (tail[0]-1, tail[1]-2):
        tail = (tail[0]-1, tail[1]-1)

    elif head == (tail[0]-2, tail[1]-1):
        tail = (tail[0]-1, tail[1]-1)
    elif head == (tail[0]+2, tail[1]-1):
        tail = (tail[0]+1, tail[1]-1)
    elif head == (tail[0]-2, tail[1]+1):
        tail = (tail[0]-1, tail[1]+1)
    elif head == (tail[0]+2, tail[1]+1):
        tail = (tail[0]+1, tail[1]+1)

    elif head == (tail[0]-2, tail[1]-2):
        tail = (tail[0]-1, tail[1]-1)
    elif head == (tail[0]+2, tail[1]+2):
        tail = (tail[0]+1, tail[1]+1)
    elif head == (tail[0]-2, tail[1]+2):
        tail = (tail[0]-1, tail[1]+1)
    elif head == (tail[0]+2, tail[1]-2):
        tail = (tail[0]+1, tail[1]-1)

    return tail

def run_rope(len_tail):
    head = (0, 0)
    tail = [(0, 0) for _ in range(len_tail)]
    seen = {tail[0]}

    for line in all_data:
        if line == "": continue
        line = line.split()
        move = dir[line[0]]
        for i in range(int(line[1])):
            head = (head[0] + move[0], head[1] + move[1])
            tail[0] = update_tail(head, tail[0])

            for j in range(1, len(tail)):
                tail[j] = update_tail(tail[j-1], tail[j])

            seen.add(tail[-1])

    return len(seen)


print("Part 1:", run_rope(1))
print("Part 2:", run_rope(9))
