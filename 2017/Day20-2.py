from _collections import defaultdict

pos, vel, acc = [], [], []

f = open("Day20.txt").read().split("\n")
i = 0
for line in f:
    a, b, c = line.split(", ")

    a = a.replace("p=<", "").replace(">", "")
    a = tuple(map(int, a.split(",")))
    pos.append(a)

    b = b.replace("v=<", "").replace(">", "")
    b = tuple(map(int, b.split(",")))
    vel.append(b)

    c = c.replace("a=<", "").replace(">", "")
    c = tuple(map(int, c.split(",")))
    acc.append(c)

    i += 1

n = 10000

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

p = set()
for k in range(i): p.add(k)

last = -1
for _ in range(n):
    posi = defaultdict(set)

    for j in p:
        vel[j] = add(vel[j], acc[j])
        pos[j] = add(pos[j], vel[j])
        d = abs(pos[j][0]) + abs(pos[j][1]) + abs(pos[j][2])
        posi[pos[j]].add(j)

    for k in posi.values():
        if len(k) > 1:
            for j in k:
                p.remove(j)

    if len(p) != last:
        print(len(p))
    print(len(p))

