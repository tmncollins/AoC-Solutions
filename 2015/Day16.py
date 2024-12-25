sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
       "cars": 2, "perfumes": 1}

with open("inputs/Day16.txt") as f:
    sues = f.read().split("\n")

for line in sues:
    if len(line) < 5: continue

    line = line.replace(":", "").replace(",", "").split()
    num = int(line[1])

    correct1 = True
    correct2 = True
    for i in range(2, len(line), 2):
        item = line[i]
        item_num = int(line[i+1])

        # part 1
        if sue[item] != item_num:
            correct1 = False

        if item in ["cats", "trees"]:
            if sue[item] >= item_num:
                correct2 = False
        elif item in ["pomeranians", "goldfish"]:
            if sue[item] <= item_num:
                correct2 = False
        else:
            if sue[item] != item_num:
                correct2 = False

    if correct1:
        print("Part 1:", num)
    if correct2:
        print("Part 2:", num)
