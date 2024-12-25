import heapq

def solve(eq1, eq2):
    f = eq1[0] / eq2[0]
    eq3 = [eq2[0] * f, eq2[1] * f, eq2[2] * f]
    for i in range(3): eq3[i] = eq1[i] - eq3[i]
    g = eq1[1] / eq2[1]
    eq4 = [eq2[0] * g, eq2[1] * g, eq2[2] * g]
    for i in range(3): eq4[i] = eq1[i] - eq4[i]
    b = eq3[2] / eq3[1]
    a = eq4[2] / eq4[0]
#    print(eq3, eq4, a, b)
    if round(b, 0) != round(b, 3) or round(a, 0) != round(a, 3):
        return 0
    a = round(a, 0)
    b = round(b, 0)
    return int(a*3 + b)

def dijsktra(target, a, b):
    q = [(0, (0,0))]
    seen = set()
    while q:
        d, u = heapq.heappop(q)
        if d > 400: return 0
        if u == target:
            return d
        v1 = (u[0] + a[0], u[1] + a[1])
        d1 = d + 3
        if v1 not in seen and v1[0] <= target[0] and v1[1] <= target[1]:
            seen.add(v1)
            heapq.heappush(q, (d1,v1))
        v2 = (u[0] + b[0], u[1] + b[1])
        d2 = d + 1
        if v2 not in seen and v2[0] <= target[0] and v2[1] <= target[1]:
            seen.add(v2)
            heapq.heappush(q, (d2,v2))
    return 0

with open("inputs/Day13.txt", "r") as f:
    all_data = f.read().split("\n")

a = 0
b = 0
part1 = 0
part2 = 0
for line in all_data:
    if len(line) < 5:
        continue
    line = line.split()
    if line[1] == "A:":
        dx = int(line[2][2:-1])
        dy = int(line[3][2:])
        a = (dx, dy)
    elif line[1] == "B:":
        dx = int(line[2][2:-1])
        dy = int(line[3][2:])
        b = (dx, dy)
    else:
        x = int(line[1][2:-1])
        y = int(line[2][2:])
        part1 += solve((a[0], b[0], x), (a[1], b[1], y))
        part2 += solve((a[0], b[0], x+10000000000000), (a[1], b[1], y+10000000000000))

print("Part 1:", part1)
print("Part 2:", part2)

