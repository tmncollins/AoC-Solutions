
with open("inputs/Day1.txt") as f:
    all_data = f.read().strip().split(",")


def rot_left(x, y):
    return y, -x


def rot_right(x, y):
    return -y, x


x,y = 0, 0
dx, dy = 1, 0
seen = set()
part2 = False
for move in all_data:
    move = move.strip()
    if move[0] == "L":
        dx, dy = rot_left(dx, dy)
    elif move[0] == "R":
        dx, dy = rot_right(dx, dy)

    d = int(move[1:])
    for i in range(d):
        x += dx
        y += dy
        if (x,y) in seen and not part2:
            part2 = True
            print("Part 2:", abs(x) + abs(y))
        seen.add((x,y))

print("Part 1:", abs(x) + abs(y))

