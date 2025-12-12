from collections import defaultdict
from functools import lru_cache

f = open('inputs/Day11.txt', 'r').read().strip().split('\n')

graph = defaultdict(list)

@lru_cache(maxsize=None)
def count_paths(u):
    if u == 'out': return 1
    ans = 0
    for v in graph[u]:
        ans += count_paths(v)
    return ans

@lru_cache(maxsize=None)
def part2(u, dac=False, fft=False):
    if u == 'dac': dac = True
    if u == 'fft': fft = True
    if u == 'out':
        return dac and fft
    ans = 0
    for v in graph[u]:
        ans += part2(v, dac, fft)
    return ans

for line in f:
    start, end = line.split(': ')
    end = end.split()
    graph[start] = end

print('Part 1:', count_paths('you'))
print('Part 2:', part2('svr'))

