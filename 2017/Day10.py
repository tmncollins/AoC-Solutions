from _collections import *
from itertools import *

with open("inputs/10.txt") as f:
    lengths = list(map(int, f.read().strip().split(",")))

def run(lengths):
    global string, skip, ret
    string = deque(string)

    for l in lengths:

        s1, s2 = deque(islice(string, 0, l)), deque(islice(string, l, len(string)))
        s1.reverse()
        string = s1 + s2
        x = skip + l
        string.rotate(-x)
        ret = (ret + x) % len(string)
        skip += 1

string = [i for i in range(256)]
skip = 0
ptr = 0
ret = 0
run(lengths)
string.rotate(ret)
print("Part 1:", string[0] * string[1])

def hash(lengths):
    global string, skip, ret
    string = [i for i in range(256)]
    skip = 0
    ret = 0

    for i in range(64):
        run(lengths)

    string.rotate(ret)

    sparse = []
    for i in range(len(string) // 16):
        x = 0
        for j in range(16):
            x = x ^ string[i*16 + j]
        sparse.append(x)

    h = ""
    hex = "0123456789abcdef"

    for i in sparse:
        a = i // 16
        b = i % 16
        h += hex[a] + hex[b]

    return h


with open("inputs/10.txt") as f:
    s = f.read().strip()

lengths = [ord(i) for i in s] + [17, 31, 73, 47, 23]

print("Part 2:", hash(lengths))

