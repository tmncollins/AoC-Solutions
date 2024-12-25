import time
from collections import defaultdict

with open("inputs/Day5.txt", "r") as f:
    all_data = f.read().split("\n")

def is_ordered(pages):
    global orders
    for a,b in orders:
        if a in pages and b in pages:
            if pages.index(a) > pages.index(b):
                return False
    return True

def get_smallest(pages):
    smaller = defaultdict(int)
    for a,b in orders:
        if a in pages and b in pages:
            smaller[a] += 1
    ranked = []
    for i in pages:
        ranked.append((smaller[i], i))
    ranked = sorted(ranked)
    return ranked[-1][1]


def make_ordered(pages):
    pages = list(pages)
    new_pages = []
    while pages:
        a = get_smallest(pages)
        new_pages.append(a)
        pages.remove(a)
    return new_pages

section = 1
orders = []
pages = []
for line in all_data:
    if len(line) < 2:
        section = 2
    else:
        try:
            if section == 1:
                a, b = list(map(int, line.split("|")))
                orders.append((a,b))
            elif section == 2:
                pages.append(list(map(int, line.split(","))))
        except:
            pass

ans = 0
ans2 = 0
for p in pages:
    if is_ordered(p):
        ans += p[len(p)//2]
    else:
        p2 = make_ordered(p)
        ans2 += p2[len(p2)//2]

print("Part 1:", ans)
print("Part 2:", ans2)

