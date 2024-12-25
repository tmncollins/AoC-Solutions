from functools import lru_cache
from _collections import defaultdict

with open("inputs/Day17.txt") as f:
    containers = list(map(int, f.read().split("\n")))

ways_containers = defaultdict(int)

#@lru_cache(maxsize=None)
def count_combs(i, volume, num_containers):
    global containers

    if volume == 0:
        ways_containers[num_containers] += 1
        return 1
    if i >= len(containers): return 0

    combs = 0
    if volume >= containers[i]:
        combs += count_combs(i+1, volume - containers[i], num_containers+1)
    combs += count_combs(i+1, volume, num_containers)

    return combs


print("Part 1:", count_combs(0, 150, 0))
print("Part 2:", ways_containers[min(ways_containers.keys())])

