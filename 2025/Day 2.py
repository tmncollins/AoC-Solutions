import re

f = open('inputs/Day2.txt', 'r').read().strip().split(',')

part1 = 0
part2 = 0
regex = re.compile(r'^(\d+)\1+$')

for pair in f:
    a,b = list(map(int, pair.split('-')))
    for i in range(a, b+1):
        x = str(i)
        #
        mid = len(x) // 2
        if x[:mid] == x[mid:]: part1 += i
        if re.match(regex, x):
            part2 += i


print('Part 1:', part1)
print('Part 2:', part2)
