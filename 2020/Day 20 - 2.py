seaMonster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")

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
    # top 2
    e.append(tile[0])
    e.append(tile[0][::-1])
    # bot 2
    e.append(tile[-1])
    e.append(tile[-1][::-1])
    a = ""
    b = ""
    for i in range(len(tile)):
        a += tile[i][0]
        b += tile[i][-1]
    # left 2
    e.append(a)
    e.append(a[::-1])
    # right 2
    e.append(b)
    e.append(b[::-1])

    return e

#print(tiles, ids)

for i in range(len(ids)):
    edges.append(processTile(tiles[i]))

from _collections import defaultdict
count = defaultdict(int)

match = defaultdict(list)

def getIntersect(tileC, tileN):
    eC = processTile(tileC)
    eN = processTile(tileN)
    for side in eC:
        if side in eN:
            return (eC.index(side) // 2, eN.index(side) // 2)

for i in range(len(ids)):
    for side in edges[i]:
        for j in range(len(ids)):
            if i != j:
                if side in edges[j]:
                    count[ids[i]] += 1
                    match[ids[i]].append(ids[j])

corners = []
for k,v in count.items():
    if v == 4:
        corners.append(k)

def rotate(id):
    tile = tiles[ids.index(id)]
    next = []
    """    for col in range(len(tile[0])):
        r = ""
        for row in range(len(tile)):
            r += tile[col][len(tile)-1-row]
        next.append(r)
    """
    a = list(zip(*tile[::-1]))
    for item in a:
        next.append("".join(item))
    tiles[ids.index(id)] = next

def placeTile(tileA, pos):
    global big
    x,y = -1, -1
    for i in range(len(big)):
        line = big[i]
        if tileA in line:
            x,y = line.index(tileA), i
            break
    if x == -1:
        return False, x, y
    if pos == 0:
        # up
        if y > 0:
            if big[y-1][x] == 0:
                return True, x,y-1
        return False, x, y
    if pos == 1:
        # down
        if y < len(big) - 1:
            if big[y + 1][x] == 0:
                return True, x, y+1
        return False, x, y
    if pos == 2:
        # left
        if x > 0:
            if big[y][x-1] == 0:
                return True, x-1, y
        return False, x, y
    if pos == 3:
        # right
        if x < len(big[0]) - 1:
            if big[y][x+1] == 0:
                return True, x+1,y
        return False, x, y

    return False, x, y

def flip(id, ud):
    global tiles
    id = ids.index(id)
    if ud:
        # flip up / down
        tiles[id] = tiles[id][::-1]
    else:
        # flip left / right
        next = []
        for item in tiles[id]:
            next.append(item[::-1])
        tiles[id] = next

def getR(a,b):
    if a == 0:
        if b == 0: return 2
        if b == 2: return 3
        if b == 3: return 1
    elif a == 1:
        if b == 1: return 2
        if b == 2: return 1
        if b == 3: return 3
    elif a == 2:
        if b == 0: return 1
        if b == 2: return 2
        if b == 1: return 3
    else:
        if b == 0: return 3
        if b == 3: return 2
        if b == 1: return 1

    return 0

def printTile(id):
    id = ids.index(id)
    for line in tiles[id]:
        print(line)
    print()

def assemble():
    seen = set()
    global big
    big = [[0 for _ in range(24)] for _ in range(24)]
    pending = [corners[0]]
    big[11][11] = corners[0]
    while pending:
        curr = pending.pop(0)
        for id in match[curr]:
            if id not in seen:
                seen.add(id)
                pending.append(id)
                tileC = tiles[ids.index(curr)]
                tileN = tiles[ids.index(id)]
                r = 0
                sideC, sideN = getIntersect(tileC, tileN)

#                print(tileC, tileN, sideC, sideN)

                # try placing sideN next to sideC
                placed,x,y = placeTile(curr, sideC)
                print(placed, x,y, sideC)
#                placed = True
                if placed:
                    big[y][x] = id
                else:
                    # flip the tile
                    if sideN < 2:
                        # flip top / bottom
                        flip(curr, True)
                    else:
                        # flip left / right
                        flip(curr, False)
                    tileC = tiles[ids.index(id)]
                    sideC, sideN = getIntersect(tileC, tiles[ids.index(id)])
                    print(sideC)
                    placed, x, y = placeTile(curr, sideC)
#                    placed = True
                    print(big, x,y)
                    if placed:
                        big[y][x] = id
                    else:
                        print("CANNOT PLACE!")

                        printTile(curr)
                        printTile(id)
                        input()
                # rotate the tile
                for i in range(getR(sideC, sideN)):
                    rotate(id)
                    printTile(id)

    for line in big:
        print(line)
assemble()


