
with open("inputs/Day8.txt") as f:
    all_data = f.read().split("\n")


height = 6
width = 50
grid = [[0 for _ in range(width)] for _ in range(height)]

def output(x,y):
    for i in range(y):
        line = ""
        for j in range(x):
            if grid[i][j] == 1:
                line += "#"
            else: line += " "
        print(line)

for line in all_data:
    if len(line) < 5: continue

    line = line.split()
    if line[0] == "rect":
        x, y = list(map(int, line[1].split("x")))
        for i in range(y):
            for j in range(x):
                grid[i][j] = 1
    elif line[0] == "rotate":
        if line[1] == "row":
            row = int(line[2].replace("y=", ""))
            x = int(line[4])
            for i in range(x):
                grid[row].insert(0, (grid[row].pop()))
        elif line[1] == "column":
            col = int(line[2].replace("x=", ""))
            x = int(line[4])
            for i in range(x):
                a = grid[-1][col]
                for j in range(height-1, 0, -1):
                    grid[j][col] = grid[j-1][col]
                grid[0][col] = a


part1 = 0
for y in range(height):
    for x in range(width):
        part1 += grid[y][x]

print("Part 1:", part1)
output(width, height)
print()

