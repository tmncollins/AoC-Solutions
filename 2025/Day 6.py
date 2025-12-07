from math import prod

f = open('inputs/Day6.txt', 'r').read().strip().split("\n")

cols = []

for line in f:
    line = line.split()
    if len(cols) == 0:
        cols = [[] for _ in range(len(line))]
    for i in range(len(cols)):
        cols[i].append(line[i])

part1 = 0
for c in cols:
    col, op = list(map(int, c[:-1])), c[-1]
    if op == '+': part1 += sum(col)
    elif op == '*': part1 += prod(col)

print('Part 1:', part1)

f = open('inputs/Day6.txt', 'r').read().strip().split("\n")

part2 = 0
operators = [f[-1][0]]
MAX_WIDTH = 0
for i in range(len(f)-1): MAX_WIDTH = max(MAX_WIDTH, len(f[i]))
while len(f[-1]) < MAX_WIDTH+1: f[-1] += ' '
f[-1] += '+'

positions = [0]
for i in range(1, len(f[-1])):
    if f[-1][i] in '+*':
        width = i - positions[-1]
        positions.append(i)

        nums = []
        for n in range(width-1):
            num = ''
            for j in range(len(f)-1):
                try:
                    num += f[j][n]
                except:
                    num += ''
            nums.append(int(num))

        if operators[-1] == '*': part2 += prod(nums)
        else: part2 += sum(nums)

        for j in range(len(f)-1):
            f[j] = f[j][width:]


        operators.append(f[-1][i])

print('Part 2:', part2)

