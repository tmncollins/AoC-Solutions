with open("inputs/Day17.txt") as f:
    all_data = f.read().strip()

#all_data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

rocks = [[(2,0), (3,0), (4,0), (5,0)],
         [(2,1), (3,1), (4,1), (3,0), (3,2)],
         [(2,0), (3,0), (4,2), (4,1), (4,0)],
         [(2,0), (2,1), (2,2), (2,3)],
         [(2,0), (2,1), (3,0), (3,1)]]


def can_move(rock, move):
    global floor

    for r in rock:
        x = r[0] + move[0]
        y = r[1] + move[1]
        if (x,y) in floor: return False
        if x < 0 or x >= 7: return False

    return True


def move_rock(r, move):

    for j in range(len(r)):
        r[j] = (r[j][0] + move[0], r[j][1] + move[1])


floor = {(i, 0) for i in range(7)}

height = 4

ptr = 0
moves = []

for m in all_data:
    if m == "<": moves.append((-1, 0))
    elif m == ">": moves.append((1,0))


def output():
    global height, floor

    for y in range(height, 0, -1):
        line = "|"
        for x in range(7):
            if (x,y) in floor:
                line += "#"
            else: line += " "
        line += "|"
        print(line)
    print("+-------+")


heights = []
target = 1000000000000
heights.append(0)
for i in range(20000):
    r = list(rocks[i%5])

#    print(r)

    for j in range(len(r)):
        r[j] = (r[j][0], r[j][1] + height)

    # fall
    cnt = 0
#    print(height, r)
    while True:
        # move left/right
        if can_move(r, moves[ptr]):
            move_rock(r, moves[ptr])
        ptr = (ptr + 1) % len(moves)
        # move down
        if can_move(r, (0, -1)):
            move_rock(r, (0, -1))
        else:
            break
        cnt += 1



    for p in r: floor.add(p)

    # update height
    for x, y in r:
        height = max(height, y+4)

    if i % 5 == 4:
        heights.append(height-4)

    if i == 2021:
        print("Part 1:", height - 4)


# get arithmetic sequence
def get_seq(target):
    target = target // 5
    end = len(heights) // 3
    end = min(target, end)
    for start in range(end):
        for second in range(start + 1, end):
            d = heights[second] - heights[start]
            x = second - start
            ptr = second
            valid = True
            cnt = 0
            while ptr < len(heights):
                if heights[ptr] - heights[ptr - x] != d:
                    valid = False
                    break
                cnt += 1
                ptr += x
            if valid:
                t = target - start
                if t % x == 0:
                    return start, x, d


def get_target(target):
    start, x, d = get_seq(target)
    target = target // 5
    target -= start
    t = target // x
    return heights[start] + t * d


t = 1000000000000
print("Part 2:", get_target(t))