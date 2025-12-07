
f = open('inputs/Day1.txt', 'r').read().strip().split("\n")

pos = 50

part1 = 0
part2 = 0

for cmd in f:
    d, v = cmd[0], int(cmd[1:])
    if d == 'L':
        for i in range(v):
            pos -= 1
            if pos == 0: part2 += 1
            if pos < 0: pos += 100
    else:
        for i in range(v):
            pos += 1
            if pos > 99: pos -= 100
            if pos == 0: part2 += 1
    if pos == 0: part1 += 1


print("Part 1:", part1)
print("Part 2:", part2)