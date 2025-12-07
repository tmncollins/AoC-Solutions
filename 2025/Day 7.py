from collections import defaultdict

f = open('inputs/Day7.txt', 'r').read().strip().split("\n")

beams = defaultdict(int)
beams[f[0].index('S')] = 1
part1 = 0
for i in range(1, len(f)):
#    print(f'{i} out of {len(f)}')
    new_beams = defaultdict(int)
    for b in beams.keys():
        if f[i][b] == '^':
            new_beams[b-1] += beams[b]
            new_beams[b+1] += beams[b]
            part1 += 1
        else:
            new_beams[b] += beams[b]
    beams = new_beams

print('Part 1:', part1)
print('Part 2:', sum(beams.values()))
