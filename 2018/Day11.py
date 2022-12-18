serial_number = 2568

power_cell = [[0 for i in range(300)] for j in range(300)]

for y in range(1, 301):
    for x in range(1,301):
        rack_id = x + 10
        power = rack_id * y
        power += serial_number
        power *= rack_id
        power %= 1000
        power //= 100
        power -= 5
        power_cell[y-1][x-1] = int(power)


max_loc = None

cum_x = [[0 for i in range(301)] for j in range(301)]
for y in range(300):
    for x in range(300):
        cum_x[y+1][x+1] = cum_x[y+1][x] + power_cell[y][x]
cum_y = [[0 for i in range(301)] for j in range(301)]
for y in range(300):
    for x in range(300):
        cum_y[y+1][x+1] = cum_y[y][x+1] + power_cell[y][x]

max_size = 3
max_sqr = -float("inf")
for size in range(3,301):

    for y in range(300 - size + 1):
        sqr = 0
        for dy in range(size):
            sqr += cum_x[y+dy+1][size-1]

        for x in range(300 - size + 1):
            sqr += cum_y[y+size][x+size] - cum_y[y][x+size]
            sqr -= cum_y[y+size][x] - cum_y[y][x]
#            print(x,y,sqr)
            if sqr > max_sqr:
                max_sqr = sqr
                max_loc = (x + 1, y + 1)
                max_size = size
    if size == 3:
        print("Part 1:", max_loc)
#    print(size)
print("Part 2:", max_loc, max_size)
