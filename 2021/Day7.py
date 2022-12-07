f = open("Day7.txt")
data = f.read().split("\n")
crabs = list(map(int, data[0].split(",")))
a = min(crabs)
b = max(crabs)

ans = float("inf")
for p in range(a, b+1):
    fuel = 0
    for c in crabs:
        fuel += abs(c - p)
    ans = min(ans, fuel)

print("Part 1:", ans)

ans = float("inf")
for p in range(a, b+1):
    fuel = 0
    for c in crabs:
        d = abs(c - p)
        d = (d * (d+1)) / 2
        fuel += d
    ans = min(ans, fuel)

print("Part 2:", int(ans))