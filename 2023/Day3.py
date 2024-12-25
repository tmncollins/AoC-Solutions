from math import prod

with open("inputs/Day3.txt") as file:
    data = file.read().split()

non_symbols = "0123456789."
digits = "0123456789"
move = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,1), (1,0), (1,-1)]
part1 = 0
part2 = 0
seen = set()

def get_number(x,y):
#    print(x, y, data[y][x])
    if data[y][x] not in digits: return -1, -1

    while x >= 0 and data[y][x] in digits: x -= 1
    x += 1
    left = x + y*len(data[y])
    number = ""
    while x < len(data[y]) and data[y][x] in digits:
        number += data[y][x]
        x += 1
    return int(number), left


for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] not in non_symbols:
            numbers = []
            small_seen = set()
            for dx, dy in move:
                n, i = get_number(x+dx, y+dy)
                if i != -1 and i not in small_seen:
                    small_seen.add(i)
                    numbers.append(n)
                if i != -1 and i not in seen:
#                    print(n, i)
                    seen.add(i)
                    part1 += n
            if data[y][x] == "*" and len(numbers) == 2:
                part2 += prod(numbers)

print(part1)
print(part2)
