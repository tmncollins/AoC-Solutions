with open("input/13.txt") as f:
    track = f.read().split("\n")

carts = []

for y in range(len(track)):
    for x in range(len(track[y])):
        if track[y][x] == "^":
            carts.append([x,y,0,-1,0])
        elif track[y][x] == "<":
            carts.append([x,y,-1,0,0])
        elif track[y][x] == ">":
            carts.append([x,y,1,0,0])
        elif track[y][x] == "v":
            carts.append([x,y,0,1,0])

locations = set()
for cart in carts:
    locations.add((cart[0], cart[1]))


def turn_left(dx,dy):
    return dy, -dx

def turn_right(dx,dy):
    return -dy, dx

def output():
    global carts, track
    locs = set()
    for c in carts: locs.add((c[0], c[1]))

    for y in range(len(track)):
        for x in range(len(track[y])):
            if (x,y) in locs:
                print("#",end="")
            else:
                print(track[y][x],end="")
        print()

part1 = False

while carts:
    carts = sorted(carts)
    new_carts = []
    crashed = set()
    locations = set()
    for c in carts:
        locations.add((c[0], c[1]))

#    print(carts)

    if len(carts) == 1:
        print("Part 2:", carts[0][0], carts[0][1])
        break

    for x,y,dx,dy,i in carts:

        if (x,y) in crashed:
            continue

        if track[y][x] == "\\":
            dx,dy = dy,dx
        elif track[y][x] == "/":
            dx,dy = -dy,-dx
        elif track[y][x] == "+":
            if i == 0:
                i = 1
                dx,dy = turn_left(dx,dy)
            elif i == 1:
                i = 2
            else:
                i = 0
                dx,dy = turn_right(dx,dy)

        locations.remove((x,y))

        x += dx
        y += dy

        if (x,y) in locations:
            if not part1:
                print("Part 1:", x, y)
                part1 = True
            crashed.add((x,y))

        else:
            new_carts.append([x,y,dx,dy,i])
            locations.add((x,y))

    carts = []

    for cart in new_carts:
        if (cart[0], cart[1]) not in crashed:
            carts.append(cart)




