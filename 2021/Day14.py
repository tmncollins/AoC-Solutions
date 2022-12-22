from _collections import defaultdict

data = open("inputs/Day14.txt").read().split("\n")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

p = data[0]
last = p[-1]
rules = dict()
polymer = defaultdict(int)

for i in range(len(p) - 1):
    r = p[i] + p[i+1]
    polymer[r] += 1

for i in range(2, len(data)):
    l = data[i].split(" -> ")
    rules[l[0]] = l[1]

def score(polymer, last=""):
    d = []
    for a in alpha:
        s = 0
        if a == last: s += 1
        for i in polymer.keys():
            if a == i[0]:
                s += polymer[i]
        if s > 0:
            d.append((s, a))
    d = sorted(d)
    return d[-1][0] - d[0][0]


for j in range(40):
    p2 = defaultdict(int)
    for i in polymer.keys():
#        print(i)
        a = rules[i]
        n1 = i[0] + a
        n2 =  a + i[1]
        p2[n1] += polymer[i]
        p2[n2] += polymer[i]
    polymer = dict(p2)
#    print(polymer, last)

    if j == 9:
        print("Part 1:", score(polymer, last))

print("Part 2:", score(polymer, last))

