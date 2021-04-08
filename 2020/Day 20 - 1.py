with open('inputs/20.txt', 'r') as f: #open the file
    contents = f.readlines()

ids = []
tiles = [[]]
for line in contents:
    if line.startswith("Tile"):
        line = line.split()[1].replace(":", "")
        ids.append(line)
    elif line == "\n":
        tiles.append([])
    else:
        tiles[-1].append(line.replace("\n", ""))


edges = []


def processTile(tile):
    e = []
    e.append(tile[0])
    e.append(tile[0][::-1])
    e.append(tile[-1])
    e.append(tile[-1][::-1])
    a = ""
    b = ""
    for i in range(len(tile)):
        a += tile[i][0]
        b += tile[i][-1]
    e.append(a)
    e.append(a[::-1])
    e.append(b)
    e.append(b[::-1])

    return e

#print(tiles, ids)

for i in range(len(ids)):
    edges.append(processTile(tiles[i]))

from _collections import defaultdict
count = defaultdict(int)

for i in range(len(ids)):
    for side in edges[i]:
        for j in range(len(ids)):
            if i != j:
                if side in edges[j]:
                    count[ids[i]] += 1

tot = 1
for k,v in count.items():
    if v == 4:
        tot *= int(k)
print(tot)
