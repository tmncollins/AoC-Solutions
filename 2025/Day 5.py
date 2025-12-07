f = open('inputs/Day5.txt', 'r').read().strip().split('\n')

def overlap(r1, r2):
    if r1[0] <= r2[0] <= r1[1]: return True
    if r2[0] <= r1[0] <= r2[1]: return True
    return False

def merge(r1, r2):
    MIN = min(min(r1), min(r2))
    MAX = max(max(r1), max(r2))
    return [MIN, MAX]

def in_range(r, i):
    return r[0] <= i <= r[1]

ranges = []
ids = []

for line in f:
    if '-' in line:
        r = list(map(int, line.split('-')))
        ranges.append(r)
    elif len(line) > 0:
        ids.append(int(line))

ranges = sorted(ranges)
print(ranges)
new_ranges = [ranges[0]]
for i in range(1, len(ranges)):
    if overlap(new_ranges[-1], ranges[i]):
        new_ranges[-1] = merge(new_ranges[-1], ranges[i])
    else:
        new_ranges.append(ranges[i])
ranges = new_ranges
print(ranges)

part1 = 0
for i in ids:
    flag = False
    for r in ranges:
        if in_range(r, i):
            flag = True
            break
    if flag:
        print(i)
        part1 += 1

print('Part 1:', part1)

part2 = 0
for i in range(len(ranges)):
    part2 += ranges[i][1] + 1 - ranges[i][0]
print('Part 2:', part2)
