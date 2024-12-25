from _collections import defaultdict
from functools import lru_cache

with open("inputs/Day22.txt") as file:
    data = file.read().strip().split("\n")

# bricks to be stored as z,x,y
all_bricks = set()
brick_index = dict()
highest_z = defaultdict(int)

#@lru_cache(maxsize=None)
def count_fall_helper(idx):
#    print(idx)
    global falling
    if idx in falling: return 0
    falling.add(idx)
    ans = 1
    brick = fallen_bricks[idx]
    for z,x,y in brick:
        above = (z+1, x, y)
        if above in all_bricks and brick_index[above] != idx:
            # see if this brick is supported by any other brick
            idx2 = brick_index[above]
            brick2 = fallen_bricks[idx2]
            supported = False
            for z2,x2,y2 in brick2:
                if z2-1 == 0:
                    supported = True # supported by ground
                    break
                below = (z2-1, x2, y2)
                if below in all_bricks and brick_index[below] not in [idx, idx2] and brick_index[below] not in falling:
                    supported = True # supported by another brick
                    break
            if not supported:
                ans += count_fall_helper(idx2)
    return ans

def count_fall(idx):
    global falling
    falling = set()
    return count_fall_helper(idx) - 1


def get_brick(a, b):
    bricks = []
    if a[0] != b[0]:
        for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
            bricks.append((i, a[1], a[2]))
    elif a[1] != b[1]:
        for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
            bricks.append((a[0], i, a[2]))
    elif a[2] != b[2]:
        for i in range(min(a[2], b[2]), max(a[2], b[2])+1):
            bricks.append((a[0], a[1], i))
    else:
        bricks.append((a[0], a[1], a[2]))

    return bricks

def set_z(brick, z):
#    print(brick)
    dz = z - brick[0][0]
    for i in range(len(brick)):
        brick[i] = (brick[i][0] + dz, brick[i][1], brick[i][2])
    return brick

def can_disintegrate(idx):
    brick = fallen_bricks[idx]
    for z,x,y in brick:
        above = (z+1, x, y)
        if above in all_bricks and brick_index[above] != idx:
            # see if this brick is supported by any other brick
            idx2 = brick_index[above]
            brick2 = fallen_bricks[idx2]
            supported = False
            for z2,x2,y2 in brick2:
                if z2-1 == 0:
                    supported = True # supported by ground
                    break
                below = (z2-1, x2, y2)
                if below in all_bricks and brick_index[below] not in [idx, idx2]:
                    supported = True # supported by another brick
                    break
            if not supported:
                return False
    return True

bricks = []
for line in data:
    a, b = line.split("~")
    a = list(map(int, a.split(",")))
    a = [a[2], a[0], a[1]]
    b = list(map(int, b.split(",")))
    b = [b[2], b[0], b[1]]
    brick = get_brick(a, b)
    bricks.append(brick)

bricks = sorted(bricks)

#print(bricks)

fallen_bricks = []
# make them fall
for brick in bricks:
    max_z = 0
    for z,x,y in brick:
        max_z = max(max_z, highest_z[(x,y)])
    brick = set_z(brick, max_z + 1)
    for z,x,y in brick:
        highest_z[(x,y)] = max(highest_z[(x,y)], z)
        all_bricks.add((z,x,y))
        brick_index[(z,x,y)] = len(fallen_bricks)
    fallen_bricks.append(brick)

part1 = 0
for brick in fallen_bricks:
#    print(brick)
    if can_disintegrate(brick_index[brick[0]]):
        part1 += 1

part2 = 0
for brick in fallen_bricks:
#    print(brick_index[brick[0]], len(fallen_bricks))
    x = count_fall(brick_index[brick[0]])
#    print(x)
    part2 += x

print("Part 1:", part1)
print("Part 2:", part2)



