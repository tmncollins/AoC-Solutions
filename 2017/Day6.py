
from collections import defaultdict

with open("inputs/6.txt") as f:
    banks = list(map(int, f.read().strip().split()))

cnt = 0

seen = defaultdict(int)
seen[tuple(banks)] = 1

while True:

    cnt += 1

    max_bank = 0
    max_bank_mem = 0
    for i in range(len(banks)):
        if banks[i] > max_bank_mem:
            max_bank_mem = banks[i]
            max_bank = i

    banks[max_bank] = 0
    ptr = max_bank
    for i in range(max_bank_mem):
        ptr = (ptr + 1) % len(banks)
        banks[ptr] += 1

    b = tuple(banks)

    if seen[b] == 0:
        seen[b] = cnt+1

    else:
        print("Part 1:", cnt)
        print("Part 2:", cnt + 1 - seen[b])
        break
