
def fit(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5: return False
    return True

def process_lock(rect):
    global locks, keys
    heights = []
    for x in range(5):
        for y in range(6, -1, -1):
            if rect[y][x] == "#":
                heights.append(y)
                break
    locks.append(heights)

def process_key(rect):
    global locks, keys
    heights = []
    for x in range(5):
        for y in range(0, 7, 1):
            if rect[y][x] == "#":
                heights.append(6-y)
                break
    keys.append(heights)

def process(rect):
    is_lock = rect[0][0] == "#"
    if is_lock: process_lock(rect)
    else: process_key(rect)

all_data = open("inputs/Day25.txt").read().split("\n")
keys = []
locks = []

rect = []
for line in all_data:
    if len(line) < 3:
        process(rect)
        rect = []
    else:
        rect.append(line)
if len(rect) > 0:
    process(rect)

#print(keys, locks)

ans = 0
for k in keys:
    for l in locks:
        if fit(k, l):
            ans += 1
print("Part 1:", ans)
