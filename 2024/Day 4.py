import time
from collections import defaultdict

with open("inputs/Day4.txt", "r") as f:
    grid = f.read().split("\n")

Y = len(grid)
X = len(grid[0])

def in_grid(x,y):
    if x < 0 or y < 0 or x >= X or y >= Y: return False
    return True

# === PART 1 ===
def check_xmas(x,y):
    directions = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
    word = "XMAS"
    ans = 0
    for d in directions:
        _x, _y = x, y
        found = True
        for i in range(1,4):
            _x += d[0]
            _y += d[1]
            if not in_grid(_x, _y) or grid[_y][_x] != word[i]:
                found = False
                break
        if found:
            ans += 1
    return ans

def count_xmas():
    ans = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == "X":
                ans += check_xmas(x,y)
    return ans

# === PART 2 ===
def check_x_mas(x,y):
    word = "XMAS"
    if x < 1 or y < 1: return 0
    if x >= X-1 or y >= Y-1: return 0

    if (grid[y-1][x-1] == "S" and grid[y+1][x+1] == "M") or (grid[y-1][x-1] == "M" and grid[y+1][x+1] == "S"):
        if (grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M") or \
           (grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S"):
            return 1
    return 0

def count_x_mas():
    ans = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == "A":
                ans += check_x_mas(x,y)
    return ans


print("Part 1:", count_xmas())
print("Part 2:", count_x_mas())

