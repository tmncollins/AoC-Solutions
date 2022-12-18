import heapq

with open("input/15.txt") as f:
    all_data = f.read().split("\n")

def run(elf_attack = 3, goblin_attack = 3, debug=0, part2 = False):

    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    # UNIT: Y, X, TYPE, HEALTH
    walls = set()
    goblins = set()
    elves = set()
    units = dict()

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def free(pos):
        return pos not in walls and pos not in elves and pos not in goblins

    def get_best_move(pos, targets):
        q = []
        for t in targets:
            heapq.heappush(q, (dist(t, pos), 0, t))
        seen = set()

        # A* search
        while q:
            x, d, p = heapq.heappop(q)
            for m in moves:
                np = (p[0] + m[0], p[1] + m[1])
                if np == pos:
                    # found best possible move
                    return p
                elif free(np) and np not in seen:
                    # can move here
                    seen.add(np)
                    heapq.heappush(q, (dist(np, pos) + d + 1, d + 1, np))

        return None # no valid move

    width, height = 0, len(all_data)

    def output():
        for y in range(height):
            line = ""
            for x in range(width):
                if (y,x) in walls: line += "#"
                elif (y,x) in elves: line += "E"
                elif (y,x) in goblins: line += "G"
                else: line += "."
            print(line)
        print()

    for y in range(len(all_data)):
        width = max(width, len(all_data[y]))
        for x in range(len(all_data[y])):
            if all_data[y][x] == "#":
                walls.add((y,x))
            elif all_data[y][x] == "G":
                goblins.add((y,x))
                units[(y,x)] = ["G", 200]
            elif all_data[y][x] == "E":
                elves.add((y,x))
                units[(y,x)] = ["E", 200]

    free_elf = set()
    free_goblin = set()

    for pos in goblins:
        for m in moves:
            np = (pos[0] + m[0], pos[1] + m[1])
            if free(np): free_goblin.add(np)
    for pos in elves:
        for m in moves:
            np = (pos[0] + m[0], pos[1] + m[1])
            if free(np): free_elf.add(np)

    round = 0
    while len(elves) > 0 and len(goblins) > 0:
        pos = sorted(units.keys())

        if debug >= 2:
            print("Round:", round)
            if debug >= 3:
                print(units)
            output()
#        input()

        for y,x in pos:

            if len(goblins) == 0 or len(elves) == 0:
                round -= 1
                break

            if (y,x) not in units: continue # we died sadly

            race, health = units[(y,x)]

            if race == "E":
                free_goblin = set()
                for pos in goblins:
                    for m in moves:
                        np = (pos[0] + m[0], pos[1] + m[1])
                        if free(np): free_goblin.add(np)
            else:
                free_elf = set()
                for pos in elves:
                    for m in moves:
                        np = (pos[0] + m[0], pos[1] + m[1])
                        if free(np): free_elf.add(np)

            if race == "E":
                # are we next to a goblin?
                attack = False
                for m in moves:
                    if (y + m[0], x + m[1]) in goblins:
                        attack = True
                        break

                if not attack:

                    if len(free_goblin) == 0: continue # nothing to see here

                    new_pos = get_best_move((y,x), free_goblin)
                    if new_pos == None: continue # nothing to see here

                    # update position info
                    if new_pos in free_goblin: free_goblin.remove(new_pos)
                    units.pop((y,x))
                    elves.remove((y,x))
                    elves.add(new_pos)
                    units[new_pos] = [race, health]
                    for m in moves:
                        p = (y + m[0], x + m[1])
                        p2 = (y + m[0]*2, x + m[1]*2)
                        if p in free_elf and p2 not in elves: free_elf.remove(p)
                        if p in elves: free_elf.add((y,x))
                        if p in goblins: free_goblin.add((y,x))

                        p = (new_pos[0] + m[0], new_pos[1] + m[1])
                        if free(p):
                            free_elf.add(p)
                    y,x = new_pos

                # attack!
                can_attack = []
                for m in moves:
                    p = (y + m[0], x + m[1])
                    if p in goblins:
                        can_attack.append([units[p][1], p])
                can_attack = sorted(can_attack)

                if len(can_attack) == 0: continue # nothing to see here

                target = can_attack[0][1]
                units[target][1] -= elf_attack

                if units[target][1] <= 0:
                    # unit is dead, remove its corpse
                    goblins.remove(target)
                    units.pop(target)
                    for m in moves:
                        p = (target[0] + m[0], target[1] + m[1])
                        p2 = (target[0] + m[0]*2, target[1] + m[1]*2)
                        if p in free_goblin and p2 not in goblins: free_goblin.remove(p)
                        if p in elves: free_elf.add((target[0], target[1]))
                        if p in goblins: free_goblin.add((target[0], target[1]))

            else:
                # are we next to an elf?
                attack = False
                for m in moves:
                    if (y + m[0], x + m[1]) in elves:
                        attack = True
                        break

                if not attack:
                    if len(free_elf) == 0: continue # nothing to see here

                    new_pos = get_best_move((y,x), free_elf)
#                    print(y,x, free_elf, new_pos)
                    if new_pos == None: continue # nothing to see here

                    # update position info
                    if new_pos in free_elf: free_elf.remove(new_pos)
                    units.pop((y,x))
                    goblins.remove((y,x))
                    goblins.add(new_pos)
                    units[new_pos] = [race, health]
                    for m in moves:
                        p = (y + m[0], x + m[1])
                        p2 = (y + m[0]*2, x + m[1]*2)
                        if p in free_goblin and p2 not in goblins: free_goblin.remove(p)
                        if p in elves: free_elf.add((y,x))
                        if p in goblins: free_goblin.add((y,x))

                        p = (new_pos[0] + m[0], new_pos[1] + m[1])
                        if free(p): free_goblin.add(p)
                    y,x = new_pos

                # attack!
                can_attack = []
                for m in moves:
                    p = (y + m[0], x + m[1])
                    if p in elves:
                        can_attack.append([units[p][1], p])
                can_attack = sorted(can_attack)

                if len(can_attack) == 0: continue # nothing to see here

                target = can_attack[0][1]
                units[target][1] -= goblin_attack

                if units[target][1] <= 0:
                    if part2:
                        return -1
#                    if debug:
#                        print("Killed an elf")
                    # unit is dead, remove its corpse
                    elves.remove(target)
                    units.pop(target)
                    for m in moves:
                        p = (target[0] + m[0], target[1] + m[1])
                        p2 = (target[0] + m[0]*2, target[1] + m[1]*2)
                        if p in free_elf and p2 not in elves: free_elf.remove(p)
                        if p in elves: free_elf.add((target[0], target[1]))
                        if p in goblins: free_goblin.add((target[0], target[1]))

        round += 1

    if debug:
        print("Round:", round)
        output()

    hp = 0
    for unit in units.values():
        hp += unit[1]

    if debug >= 3:
        print(hp)
    return hp * (round)

print("Part 1:", run(debug=1))

elf_attack = 4
while True:
    outcome = run(elf_attack = elf_attack, part2 = True)
    if outcome == -1:
        elf_attack += 1
    else:
        print(elf_attack)
        print("Part 2:", outcome)
        break