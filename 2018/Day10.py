from math import ceil, sqrt

with open("input/10.txt") as f:
    all_data = f.read().split("\n")

stars = []

for line in all_data:
    pos, vel = line.replace("position=<", "").replace(">", "").split("velocity=<")
    x,y = list(map(int, pos.split(",")))
    dx,dy = list(map(int, vel.split(",")))
    stars.append((x,y,dx,dy))


def get_in_range(min_x, min_y, max_x, max_y, stars):
    cnt = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in stars:
                cnt += 1
    return cnt


def output(min_x, min_y, max_x, max_y, stars):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in stars: print("#", end="")
            else: print(".", end="")
        print()


off_x = 40
off_y = 30

com_x = 0
x_sqr = 0
for x, y, dx, dy in stars:
    com_x += x
    x_sqr += x ** 2
com_x //= len(stars)
x_sqr //= len(stars)
var = x_sqr - com_x ** 2
spread = sqrt(sqrt(var))
last_spread = spread + 10

time = 0
while True:
    new_stars = []
    s = set()
    com_x = 0
    com_y = 0
    x_sqr = 0
    print(spread)
    if spread > 10:
        time += ceil(spread)
    else:
        time += 1
    for x,y,dx,dy in stars:
        if spread > 10:
            x += dx * ceil(spread)
            y += dy * ceil(spread)
        else:
            x += dx
            y += dy
        new_stars.append((x,y,dx,dy))
        s.add((x,y))
        com_x += x
        com_y += y
        x_sqr += x**2
    com_x //= len(stars)
    com_y //= len(stars)
    com_x = int(com_x)
    com_y = int(com_y)
    x_sqr //= len(stars)
    var = x_sqr - com_x**2
    last_spread = spread
    spread = sqrt(sqrt(var))

#    input()

    stars = new_stars
#    print(get_in_range(com_x-off_x, com_y-off_y, com_x+off_x, com_y+off_y, s))
    if spread <= 5:
#        print(s, com_x, com_y)
        print("T =", time)
        output(com_x-off_x, com_y-off_y, com_x+off_x, com_y+off_y, s)

    if spread > last_spread and spread > 6:
        output(com_x-off_x, com_y-off_y, com_x+off_x, com_y+off_y, s)
        break

"""
ZZCBGGCJ
"""
