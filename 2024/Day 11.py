from functools import lru_cache

with open("inputs/Day11.txt", "r") as f:
    stones = f.read().replace("\n", "").split()
stones = list(map(int, stones))

@lru_cache(maxsize=None)
def blink(num, times):
    if times == 0:
        return 1
    if num == 0: return blink(1, times-1)
    if len(str(num)) % 2 == 0:
        p = str(num)
        first = p[:len(p) // 2]
        second = p[len(p) // 2:]
        return blink(int(first), times-1) + blink(int(second), times-1)
    return blink(num*2024, times-1)


"""
def blink():
    global stones
    n = len(stones)
    for i in range(n):
        if stones[i] == 0:
            stones[i] = 1
        else:
            p = str(stones[i])
            if len(p) % 2 == 0:
                first = p[:len(p)//2]
                second = p[len(p)//2:]
                stones[i] = int(first)
                stones.append(int(second))
            else:
                stones[i] *= 2024

for i in range(25):
    blink()
"""

part2 = 0
part1 = 0
for i in stones:
    part1 += blink(i, 25)
    part2 += blink(i, 75)
print("Part 1:", part1)
print("Part 2:", part2)
