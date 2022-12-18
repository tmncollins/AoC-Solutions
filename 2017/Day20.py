pos, vel, acc = [], [], []

f = open("Day20.txt").read().split("\n")
i = 0
for line in f:
    a, b, c = line.split(", ")

    a = a.replace("p=<", "").replace(">", "")
    a = list(map(int, a.split(",")))
    pos.append(a)

    b = b.replace("v=<", "").replace(">", "")
    b = list(map(int, b.split(",")))
    vel.append(b)

    c = c.replace("a=<", "").replace(">", "")
    c = list(map(int, c.split(",")))
    acc.append(c)

    i += 1

n = 10000

def add(a, b):
    for i in range(3):
        a[i] += b[i]
    return a

last = -1
for _ in range(n):
    closest = 0
    closestD = float("inf")
    for j in range(i):
        vel[j] = add(vel[j], acc[j])
        pos[j] = add(pos[j], vel[j])
        d = abs(pos[j][0]) + abs(pos[j][1]) + abs(pos[j][2])
#        print(j, d)
        if d < closestD:
            closestD = d
            closest = j

    if closest != last:
        last = closest
        print(closest)


