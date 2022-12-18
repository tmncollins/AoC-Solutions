with open("input/18.txt") as f:
    all_data = f.read().split("\n")

height, width = len(all_data), 0

trees = set()
lumber = set()
clear = set()

for y in range(len(all_data)):
    width = max(len(all_data[y]), width)
    for x in range(len(all_data[y])):
        if all_data[y][x] == "|":
            trees.add((x,y))
        elif all_data[y][x] == "#":
            lumber.add((x, y))
        elif all_data[y][x] == ".":
            clear.add((x,y))

def output():
    for y in range(height):
        line = ""
        for x in range(width):
            if (x,y) in trees:
                line += "|"
            elif (x,y) in lumber:
                line += "#"
            elif (x,y) in clear:
                line += "."
            else:
                line += " "
        print(line)

def adj(x,y):
    move = [(-1,0), (1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]
    ret = []
    for m in move:
        ret.append((x+m[0], y+m[1]))
    return ret

seen = {(tuple(lumber), tuple(clear), tuple(trees)):0}
rev = {0:(lumber, clear, trees)}
target = 1000000000
part2 = False

for i in range(target):
#    if i % 20 == 0:
#        print(i, len(lumber) * len(trees))
    new_trees = set()
    new_lumber = set()
    new_clear = set()

    for x,y in clear:
        cnt = 0
        for _x,_y in adj(x,y):
            if (_x,_y) in trees:
                cnt += 1
        if cnt >= 3:
            new_trees.add((x,y))
        else:
            new_clear.add((x,y))

    for x,y in trees:
        cnt = 0
        for _x,_y in adj(x,y):
            if (_x,_y) in lumber:
                cnt += 1
        if cnt >= 3:
            new_lumber.add((x,y))
        else:
            new_trees.add((x,y))

    for x,y in lumber:
        a, b = False, False
        for _x,_y in adj(x,y):
            if (_x,_y) in lumber:
                a = True
            elif (_x,_y) in trees:
                b = True
        if a and b:
            new_lumber.add((x,y))
        else:
            new_clear.add((x,y))

    lumber = new_lumber
    clear = new_clear
    trees = new_trees

    hash = (tuple(lumber), tuple(clear), tuple(trees))
    if hash in seen and not part2:
#        print("Seen!", seen[hash])
        cyc = i+1 - seen[hash]
        target -= seen[hash]
        target %= cyc
        target += seen[hash]
        _lumber, _clear, _trees = rev[target]
        print("Part 2:", len(_lumber) * len(_trees))
        part2 = True
        break

#        break

    seen[hash] = i+1
    rev[i+1] = (lumber, clear, trees)

#    output()
#    print()

    if i == 9:
        print("Part 1:", len(lumber) * len(trees))

#print("Part 1:", len(lumber) * len(trees))

# 3 6 12 21 39 92 198 357
# +3 +6 +9 +18 +  +106