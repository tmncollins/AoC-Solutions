from _collections import deque

with open("inputs/Day16.txt") as file:
    data = file.read().strip().split("\n")


def reflect(mirror, direction):
    if mirror == "/":
        return (-direction[1], -direction[0])

    if mirror == "\\":
        return (direction[1], direction[0])

    return direction


def split(splitter, direction):
    if splitter == "-":
        if direction == (0,1) or direction == (0,-1):
            return [(-1,0), (1,0)]

    if splitter == "|":
        if direction == (1,0) or direction == (-1,0):
            return [(0,1), (0,-1)]

    return [direction]


def on_grid(x, y):
    global width, height
    if x < 0 or y < 0 or x >= width or y >= height: return False
    return True


def output():
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in energised:
                line += "#"
            else:
                line += "."
        print(line)
    print()


def add_q(pos, direction):
    global q, seen, energised
    if on_grid(pos[0], pos[1]) and (pos, direction) not in seen:
        seen.add((pos, direction))
        energised.add(pos)
        q.append([pos, direction])


def count_energised(start, start_direction):
    global q, seen, energised
    energised = set()
    seen = set()
    q = deque()
    energised.add(start)
    q.append([start, start_direction])

    while q:
        pos, direction = q.popleft()
        x,y = pos

        if data[y][x] in "/\\":
            direction = reflect(data[y][x], direction)

        elif data[y][x] in "|-":
            directions = split(data[y][x], direction)
            for direction in directions:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                add_q(new_pos, direction)

        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        add_q(new_pos, direction)

    return len(energised)


width = len(data[2])
height = len(data)

print("Part 1:", count_energised((0,0), (1,0)))

part2 = 0

for x in range(width):
    part2 = max(part2, count_energised((x, 0), (0, 1)))
    part2 = max(part2, count_energised((x, height-1), (0, -1)))

for y in range(height):
    part2 = max(part2, count_energised((0, y), (1, 0)))
    part2 = max(part2, count_energised((width-1, y), (-1, 0)))

print("Part 2:", part2)






