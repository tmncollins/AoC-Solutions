f = open('inputs/Day12.txt', 'r').read().strip().split('\n')

shapes = [0,0,0,0,0,0]
shape = 0
for i in range(0, 30, 5):
    for j in range(3):
        line = f[i+j+1]
        shapes[shape] += line.count('#')
    shape += 1

f = f[30:]
part1 = 0

for line in f:
    a, b = line.split(': ')
    a = list(map(int, a.split('x')))
    b = list(map(int, b.split()))
    total_blocks = 0
    for i in range(6):
        total_blocks += b[i] * shapes[i]
    part1 += (total_blocks < a[0] * a[1])

print('Part 1:', part1)