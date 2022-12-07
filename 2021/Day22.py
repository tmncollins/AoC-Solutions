with open("Day22.txt") as f:
    all_data = f.read().split("\n")

part2 = False

# uses simple set theory:
#
# Let N be the new cube and B be all currently on cubes
#
#   If we wish to turn N on, we want N u B
#   this is the same as N + B - (N n B)
#
#   If we wish to turn N off, we want B - (N n B)
#
# Using this, we can decompose B into many smaller cubes, called C
# (ie each cube and (N n B) we have added)
# and simply find the intersections (N n C) and sum them to get (N n B)


# returns the intersection of two cubes
def intersection(s,t):
    intersect = [-t[0], max(s[1], t[1]), min(s[2], t[2]), max(s[3], t[3]), min(s[4], t[4]), max(s[5], t[5]), min(s[6], t[6])]

    # is this a valid intersection?
    if intersect[1] > intersect[2]: return None
    if intersect[3] > intersect[4]: return None
    if intersect[5] > intersect[6]: return None

    return intersect


# cube is defined as [(-1/0/1), x_min, x_max, y_min, y_max, z_min, z_max]
# +1 means the cube has been added / turned on
#  0 means the cube has been turned off
# -1 means the cube has been removed
cubes = []
for line in all_data:

    on, line = line.split()
    on = 1 if on == "on" else 0
    x,y,z = line.replace("x=", "").replace("y=", "").replace("z=", "").split(",")
    x = list(map(int, x.split("..")))
    y = list(map(int, y.split("..")))
    z = list(map(int, z.split("..")))
    new_cube = [on, x[0], x[1], y[0], y[1], z[0], z[1]]

    if not part2:
        if max([x[1], y[1], z[1]]) > 50: continue
        if min([x[0], y[0], z[0]]) < -50: continue

    to_add = []
    # get intersection of new cube and currently added cubes
    for cube in cubes:
        intersect = intersection(new_cube, cube)
        if intersect:
            to_add.append(intersect)

    for cube in to_add:
        cubes.append(cube)

    # if this cube is to be turned on, add it also
    if on:
        cubes.append(new_cube)


def size_of(cube):
    return (cube[2] + 1 - cube[1]) * (cube[4] + 1 - cube[3]) * (cube[6] + 1 - cube[5])


def count_on(cubes):
    cnt = 0
    for cube in cubes:
        cnt += cube[0] * size_of(cube)

    return cnt

if part2:
    print("Part 2:", count_on(cubes))
else:
    print("Part 1:", count_on(cubes))
