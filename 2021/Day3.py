f = open("inputs/Day3.txt")
data = f.read().split("\n")

bits = [0 for _ in range(len(data[0]))]

for item in data:
    for i in range(len(item)):
        if item[i] == "1":
            bits[i] += 1
        else: bits[i] -= 1

g = ""
e = ""
for item in bits:
    if item > 0:
        g += "1"
        e += "0"
    else:
        g += "0"
        e += "1"

g = int(g, 2)
e = int(e, 2)

print("Part 1:", e * g)

oxy = list(data)
j = 0
while len(oxy) > 1:
    delete = []
    bits = [0 for _ in range(len(data[0]))]

    for item in oxy:
        for i in range(len(item)):
            if item[i] == "1":
                bits[i] += 1
            else:
                bits[i] -= 1

    for item in oxy:
        if (bits[j] < 0 and item[j] == "1") or (bits[j] > 0 and item[j] == "0") or (bits[j] == 0 and item[j] == "0"): delete.append(item)
    for item in delete: oxy.remove(item)

    j+=1

o = int(oxy[0], 2)

oxy = list(data)
j = 0
while len(oxy) > 1:
    delete = []
    bits = [0 for _ in range(len(data[0]))]

    for item in oxy:
        for i in range(len(item)):
            if item[i] == "1":
                bits[i] += 1
            else:
                bits[i] -= 1

    for item in oxy:
        if (bits[j] > 0 and item[j] == "1") or (bits[j] < 0 and item[j] == "0") or (bits[j] == 0 and item[j] == "1"): delete.append(item)
    for item in delete: oxy.remove(item)

    j+=1

c = int(oxy[0], 2)

print("Part 2:", o * c)