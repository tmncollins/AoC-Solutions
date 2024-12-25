from collections import defaultdict
from math import gcd

def sqr(a):
    return a**2

def distance(a, b):
#    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    return sqr(a[0]-b[0]) + sqr(a[1]-b[1])

def in_grid(pos):
    global X, Y
    x, y = pos
    if x < 0 or y < 0 or y >= Y or x >= X: return False
    return True

def is_antinode(pos, a):
    for i in range(len(a)):
        for j in range(i):
            a1 = a[i]
            a2 = a[j]
            d1 = distance(a1, pos)
            d2 = distance(a2, pos)
            d1, d2 = max(d1,d2), min(d1,d2)
#            print(d1, d2)
            if d1 == 4*d2:
                return True
    return False

def get_antinodes2(a):
    antinodes = set()
    for i in range(len(a)):
        for j in range(i):
            a1 = a[i]
            a2 = a[j]
            delta = (a1[0] - a2[0], a1[1] - a2[1])
            d = gcd(delta[0], delta[1])
            delta = (delta[0]//d, delta[1]//d)
            while in_grid(a1):
                antinodes.add(a1)
                a1 = (a1[0]+delta[0], a1[1]+delta[1])
            while in_grid(a2):
                antinodes.add(a2)
                a2 = (a2[0]-delta[0], a2[1]-delta[1])
    return antinodes

def get_antinodes(a):
    antinodes = set()
    for i in range(len(a)):
        for j in range(i):
            a1 = a[i]
            a2 = a[j]
            delta = (a1[0] - a2[0], a1[1] - a2[1])
            antinodes.add((a1[0] + delta[0], a1[1] + delta[1]))
            antinodes.add((a2[0] - delta[0], a2[1] - delta[1]))
    return antinodes

def output():
    global X, Y, grid, antinodes
    for y in range(Y):
        line = ""
        for x in range(X):
            if (x,y) in antinodes:
                line += "#"
            else:
                line += grid[y][x]
        print(line)

with open("inputs/Day8.txt", "r") as f:
    grid = f.read().split("\n")

antennae = defaultdict(set)
Y = len(grid)
X = len(grid[0])
for y in range(Y):
    for x in range(X):
        if grid[y][x] != ".":
            antennae[grid[y][x]].add((x,y))

antinodes = set()
for a in antennae.values():
    for n in get_antinodes(list(a)):
        if in_grid(n):
            antinodes.add(n)

output()
print("Part 1:", len(antinodes))

antinodes = set()
for a in antennae.values():
    for n in get_antinodes2(list(a)):
        if in_grid(n):
            antinodes.add(n)
print("Part 2:", len(antinodes))
output()
