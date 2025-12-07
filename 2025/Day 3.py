from time import time

f = open('inputs/Day3.txt', 'r').read().strip().split("\n")

start_time = time()

part1 = 0

for line in f:
    b1 = max(line[:-1])
    idx1 = line.index(b1)
    b2 = max(line[idx1+1:])
    part1 += int(b1 + b2)

print('Part 1:', part1)

part2 = 0

for line in f:
    num = ''
    idx = 0

    for i in range(12):
        b = max(line[:len(line)-11 + i])
        idx = line.index(b)+1
        line = line[idx:]
        num += b

    part2 += int(num)

print('Part 2:', part2)

print('Time Taken:', time() - start_time)