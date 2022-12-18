from collections import defaultdict

with open("inputs/7.txt") as f:
    all_data = f.read().split("\n")

weights = dict()
parent = dict()
children = dict()

name = ""

for line in all_data:
    if len(line) < 5: continue

    if "->" in line:
        p, c = line.split("->")
        name, weight = p.split()
        weight = int(weight.replace("(", "").replace(")", ""))
        weights[name] = weight
        c = c.split(",")
        children[name] = []
        for i in c:
            i = i.strip()
            parent[i] = name
            children[name].append(i)

    else:
        name, weight = line.split()
        weight = int(weight.replace("(", "").replace(")", ""))
        weights[name] = weight

while name in parent: name = parent[name]

print("Part 1:", name)

req = 0


def balance(node):
    global req

    if node not in children:
        return weights[node]

    w = []
    w2 = []
    for child in children[node]:
        child_w = balance(child)
        w.append(child_w)
        w2.append((child_w, child))

    if len(set(w)) == 1:
        return sum(w) + weights[node]

    cnt = defaultdict(int)
    for i in w:
        cnt[i] += 1
    cnt = sorted([(cnt[i], i) for i in cnt])
    correct_weight = cnt[-1][1]

    for child_w, child in w2:
        if child_w != correct_weight:
            req = correct_weight - (child_w - weights[child])
            weights[child] = req

    return len(w) * correct_weight + weights[node]


balance(name)
print("Part 2:", req)

