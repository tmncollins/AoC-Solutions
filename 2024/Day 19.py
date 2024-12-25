from functools import lru_cache

@lru_cache(maxsize=None)
def can_make(s):
    if len(s) == 0:
        return True
    global towels
    for t in towels:
        if t == s[:(len(t))]:
            if can_make(s[len(t):]): return True
    return False

@lru_cache(maxsize=None)
def count_make(s):
    if len(s) == 0:
        return 1
    global towels
    ans = 0
    for t in towels:
        if t == s[:(len(t))]:
            ans += count_make(s[len(t):])
    return ans

with open("inputs/Day19.txt", "r") as f:
    all_data = f.read().split("\n")

towels = all_data[0].split(", ")
print(towels)

part1 = 0
part2 = 0
for line in all_data:
    if "," in line or len(line) < 3: continue
    if can_make(line):
        part1 += 1
        part2 += count_make(line)

print(part1)
print(part2)