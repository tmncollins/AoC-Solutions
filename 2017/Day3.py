X = 289326
x = X

# get the shell
i = 1
while i**2 < x:
    i += 2
# change all sides to one side
x -= (i-2)**2
x %= (i-1)
print(x)
# reflect about middle
if x > i / 2:
    x = i - 1 - x
# get distance from middle
x = (i//2) - x
# add distances
print(i//2, x)
print("Part 1:", (i//2) + x)

# part 2
size = 100
x, y = size // 2, size // 2
grid = [[0 for _ in range(size)] for _ in range(size)]
grid[y][x] = 1
x += 1

move = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]

while True:
    for dx, dy in move:
        grid[y][x] += grid[y+dy][x+dx]

    if grid[y][x] >= X:
        print("Part 2:", grid[y][x])
        break

    if grid[y+1][x] != 0:
        if grid[y][x-1] == 0:
            x -= 1
        else:
            y -= 1
    elif grid[y-1][x] != 0:
        if grid[y][x+1] == 0:
            x += 1
        else:
            y += 1
    elif grid[y][x+1] != 0:
        if grid[y+1][x] == 0:
            y += 1
        else:
            x += 1
    else:
        if grid[y-1][x] == 0:
            y -= 1
        else:
            x -= 1


#print(grid)
