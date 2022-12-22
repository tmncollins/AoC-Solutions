
data = open("inputs/Day11.txt").read().split("\n")
octo = []
dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)]
flashes = 0

for line in data:
    octo.append(list(map(int, list(line))))

def valid(x, y):
    if x < 0 or y < 0: return False
    if x >= len(octo[0]) or y >= len(octo): return False
    return True

def inc():
    global octo
    for y in range(len(octo)):
        for x in range(len(octo[y])):
            octo[y][x] += 1

def flash():
    global flashes
    y = 0
    while y < len(octo):
        x = 0
        while x < len(octo):
            if octo[y][x] > 9:
                octo[y][x] = -9999
                flashes += 1
                for d in dirs:
                    if valid(x+d[0], y+d[1]):
                        octo[y+d[1]][x+d[0]] += 1
                x = 0
                y -= 1
                if y < 0: y = 0
            else:
                x += 1
        y += 1



def zero():
    for y in range(len(octo)):
        for x in range(len(octo[y])):
            if octo[y][x] < 0:
                octo[y][x] = 0

def round():
    inc()
    flash()
    zero()

n = 100
xy = len(octo) * len(octo[0])

i = 0
while True:
    if i == 100:
        print("Part 1:", flashes)
    f = flashes
    round()
#    print(i, flashes, f, xy)
    if flashes - f == xy:
        print("Part 2:", i+1)
        break
#    print(flashes)
    i += 1
#    if i == 196: break

