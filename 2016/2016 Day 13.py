from collections import deque, defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def move(x,y,num):
    if x < 0 or y < 0: return False
    v = x * x + 3 * x + 2 * x * y + y + y * y
    v += num
    v = bin(v)
    v = v.count("1")
    return v % 2 == 0

def printM(maze):
    for y in range(10):
        for x in range(10):
            a = maze[x,y]
            if a == 1: print(".", end="")
            elif a == 2: print("#", end="")
            else: print("?", end="")
        print()

def part1(num):
    global target

    pending = deque([(1,1,0)])
    dir = [(-1,0), (1,0), (0,1), (0,-1)]
    seen = set()
    while pending:
        x,y,dist = pending.popleft()
        for d in dir:
            X = x + d[0]
            Y = y + d[1]
            if (X,Y) not in seen:
                if move(X,Y,num):
                    seen.add((X, Y))
                    if (X,Y) == target:
                        return dist + 1
                    pending.append((X, Y, dist + 1))

def part2(num):
    steps = 50
    seen = set()
    pending = deque([(1,1,0)])
    dir = [(-1,0), (1,0), (0,1), (0,-1)]
    while pending:
        x,y,dist = pending.popleft()
        for d in dir:
            X = x + d[0]
            Y = y + d[1]
            if (X,Y) not in seen:
                if move(X,Y,num):
                    if dist < steps:
                        seen.add((X, Y))
                        pending.append((X, Y, dist + 1))
    return len(seen)

inp = int(input("Enter puzzle input:     "))
target = tuple(map(int, input("Enter target (X Y):    ").replace(",", " ").replace("(", "").replace(")", "").split()))

print("Part 1:", part1(inp))
print(part2(inp))