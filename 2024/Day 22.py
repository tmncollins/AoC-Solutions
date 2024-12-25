from _collections import defaultdict, deque

def evolve(n):
    mod = 16777216
    a = n * 64
    n = (n ^ a)
    n %= mod
    b = n // 32
    n = (n ^ b)
    n %= mod
    c = n * 2048
    n = (n ^ c)
    n %= mod
    return n

with open("inputs/Day22.txt", "r") as f:
    nums = f.read().split("\n")

part1 = 0
runs = defaultdict(int)
for n in nums:
    n = int(n)
    seq = deque()
    seen = set()
    last = -1
    for _ in range(2000):
        n = evolve(n)
        if last != -1:
            d = (n%10) - last
            seq.append(d)
            if len(seq) > 4: seq.popleft()
            if len(seq) == 4:
                x = tuple(seq)
                if x not in seen:
                    seen.add(x)
                    runs[x] += (n%10)

        last = n % 10
#    print(n)
    part1 += n
print("Part 1:", part1)
print("Part 2:", max(runs.values()))

