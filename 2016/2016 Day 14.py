from hashlib import md5
from _collections import deque
from functools import lru_cache
import sys

sys.setrecursionlimit(9999)

chars = list("0123456789abcdef")

inp = input("Enter puzzle input:    ").strip()

def triple(s):

    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return {s[i]}
    return set()

def quintuple(s):
    quintuples = set()
    for c in chars:
        qui = c * 5
        if qui in s:
            quintuples.add(c)
    return quintuples

def run(inp, part2 = False):
    i = 0
    keys = []
    potential_keys = deque()
    while len(keys) < 75:
        hash = md5((inp + str(i)).encode()).hexdigest()
        if part2:
            for _ in range(2016):
                hash = md5((hash).encode()).hexdigest()

        q = quintuple(hash)

        while potential_keys and i - potential_keys[0][0] >= 1000:
            potential_keys.popleft()

        if q:
            to_remove = []
            for c in q:
                for item in potential_keys:
                    if c in item[1]:
#                        print("key:", item, i)
                        keys.append(item[0])
                        to_remove.append(item)
            for item in to_remove:
                potential_keys.remove(item)

        t = triple(hash)
        if t:
            potential_keys.append((i, t))

        i += 1

    keys = sorted(keys)

    return keys[63]

print("Part 1:", run(inp))
print("Part 2:", run(inp, True))

