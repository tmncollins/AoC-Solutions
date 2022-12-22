with open("inputs/Day17.txt", "r") as f:
    all_data = f.read().replace("\n", "")

all_data = all_data.split()
print(all_data)
x = all_data[2][2:-1].split("..")
y = all_data[3][2:].split("..")
x = list(map(int, x))
y = list(map(int, y))

left = min(x)
right = max(x)
top = max(y)
bottom = min(y)


def inside(x, y):
    if x < left or x > right: return False
    if y > top or y < bottom: return False
    return True


def fire(dx, dy):
    x, y = 0, 0
    maxy = 0
    while True:
        if x > right: return -1
        if y < bottom: return -1
        x += dx
        y += dy
        maxy = max(maxy, y)
        if dx > 0: dx -= 1
        elif dx < 0: dx += 1
        dy -= 1

        if inside(x, y): return maxy

part1 = 0
part2 = 0

MAX = 400

for dx in range(MAX):
    for dy in range(-MAX, MAX):
        f = fire(dx, dy)
        if f > -1:
            part2 += 1
            part1 = max(part1, f)

print("Part 1:", part1)
print("Part 2:", part2)

