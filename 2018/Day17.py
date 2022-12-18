from time import sleep
from _collections import deque

min_x, min_y, max_x, max_y = float("inf"), float("inf"), 0, 0

with open("input/17.txt") as f:
    all_data = f.read().split("\n")

clay = set()

for line in all_data:
    if len(line) > 4:
        line = line.split(", ")
        if line[0][0] == "x":
            x = int(line[0].replace("x=", ""))
            y = list(map(int, line[1].replace("y=", "").split("..")))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, min(y))
            max_y = max(max_y, max(y))

            for _y in range(min(y), max(y) + 1):
                clay.add((x,_y))

        else:
            y = int(line[0].replace("y=", ""))
            x = list(map(int, line[1].replace("x=", "").split("..")))
            min_x = min(min_x, min(x))
            max_x = max(max_x, max(x))
            min_y = min(min_y, y)
            max_y = max(max_y, y)

            for _x in range(min(x), max(x) + 1):
                clay.add((_x,y))


water_q = deque([(500, min_y)])
settled_water = set()
falling_water = set()
max_x -= 50
min_x += 50

round = 0


def output():
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x,y) in clay: line += "#"
            elif (x,y) in falling_water: line += "|"
            elif (x,y) in settled_water: line += "~"
            else: line += "."
        print(line)

def free(x,y):
    return (x,y) not in settled_water and (x,y) not in clay

while water_q:
    round += 1
    x,y = water_q.pop()


    if round % 50000 == 0:
        for item in settled_water:
            if item in falling_water:
                falling_water.remove(item)
#        output()
#        print()
#        print(water_q)
#        print("Part 1:", len(falling_water) + len(settled_water))#    sleep(0.5)
#        input()

    if y > max_y: continue

    if free(x,y+1):
        water_q.append((x,y+1))
        falling_water.add((x,y))
    else:
        # move left and right
        left_x = x - 1
        left_stay = True
        while free(left_x, y):
            if free(left_x, y+1):
                left_x -= 1
                left_stay = False
                break
            left_x -= 1
        left_x += 1

        right_x = x + 1
        right_stay = True
        while free(right_x, y):
            if free(right_x, y+1):
                right_x += 1
                right_stay = False
                break
            right_x += 1
        right_x -= 1

        stay = left_stay and right_stay
        if stay:
            for _x in range(left_x, right_x + 1):
                settled_water.add((_x,y))

            if free(x,y-1):
                water_q.append((x,y-1))

        else:
            for _x in range(left_x, right_x + 1):
                falling_water.add((_x,y))
            if free(left_x, y+1):
                water_q.append((left_x, y+1))
            if free(right_x, y+1):
                water_q.append((right_x, y+1))


for item in settled_water:
    if item in falling_water:
        falling_water.remove(item)


output()

print("Part 1:", len(falling_water) + len(settled_water))
print("Part 2:", len(settled_water))