from _collections import deque

with open("inputs/Day18.txt") as file:
    data = file.read().strip().split("\n")

pos = (0,0)
pos_hex = (0,0)
trench = [pos]
trench_hex = [pos]
directions = {"L":(-1, 0), "U":(0,-1), "D":(0,1), "R":(1,0)}
directions_hex = {"2":(-1, 0), "3":(0,-1), "1":(0,1), "0":(1,0)}
perimeter_hex = 1
perimeter = 1

for line in data:
    line = line.split()
    if len(line) != 3: continue
    d = directions[line[0]]
    x = int(line[1])
    perimeter += x
    pos = (pos[0] + d[0]*x, pos[1] + d[1]*x)
    trench.append(pos)

    line[2] = line[2].replace("(", "").replace(")", "")
    d = directions_hex[line[2][-1]]
    x = int(line[2][1:-1], 16)
    perimeter_hex += x
    pos_hex = (pos_hex[0] + d[0]*x, pos_hex[1] + d[1]*x)
    trench_hex.append(pos_hex)

def shoelace(points):
    area = 0
    for i in range(len(points)-1):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area += points[-1][0] * points[0][1] - points[0][0] * points[-1][1]
    return area // 2

print("Part 1:", perimeter//2 + shoelace(trench) + 1)
print("Part 2:", perimeter_hex//2 + shoelace(trench_hex) + 1)

# 1904809882966
# 952404941483
# 952408144115