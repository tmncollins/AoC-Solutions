def count(output=False):
    global elves

    min_x = float("inf")
    min_y = float("inf")
    max_x = 0
    max_y = 0

    for x,y in elves:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    cnt = 0
    for y in range(min_y, max_y+1):
        line = ""
        for x in range(min_x, max_x+1):
            if (x,y) in elves: line += "#"
            else:
                line += "."
                cnt += 1
        if output:
            print(line)

    return cnt


with open("inputs/Day23.txt") as f:
    all_data = f.read().split("\n")

elves = set()
north = [(1,-1), (0,-1), (-1,-1)]
south = [(1,1), (0,1), (-1,1)]
east = [(1,-1), (1,0), (1,1)]
west = [(-1,-1), (-1,0), (-1,1)]
directions = [north, south, west, east]
moves = [(1,-1), (0,-1), (-1,-1), (1,0), (-1,0), (1,1), (0,1), (-1,1)]

for y in range(len(all_data)):
    for x in range(len(all_data[y])):
        if all_data[y][x] == "#":
            elves.add((x,y))


round = 0
while True:
    round += 1
    all_proposed = dict()
    double_proposed = set()

    for elf in elves:
        clear = True
        for m in moves:
            if (elf[0] + m[0], elf[1] + m[1]) in elves:
                clear = False
                break
        if clear: continue # no need to move

        proposed = None
        for dir in directions:
            if proposed: break
            clear = True
            for m in dir:
                if (elf[0] + m[0], elf[1] + m[1]) in elves:
                    clear = False
                    break
            if clear:
                proposed = (elf[0] + dir[1][0], elf[1] + dir[1][1])

        if proposed:
            if proposed in all_proposed:
                double_proposed.add(proposed)
            else:
                all_proposed[proposed] = elf

    for p in double_proposed:
        all_proposed.pop(p)

    for v, u in all_proposed.items():
        elves.remove(u)
        elves.add(v)

    directions.append(directions.pop(0))
#    count(True)

    if round == 10:
        print("Part 1:", count())

    if len(all_proposed) == 0:
        # finished
        print("Part 2:", round)
        break