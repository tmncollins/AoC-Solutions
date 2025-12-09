from functools import lru_cache

f = open('inputs/Day9.txt', 'r').read().strip().split()

points = []
for line in f:
    x, y = list(map(int, line.split(',')))
    points.append((x,y))

def area(a, b):
    x1, x2 = min(a[0], b[0]), max(a[0], b[0])
    y1, y2 = min(a[1], b[1]), max(a[1], b[1])
    return (y2+1-y1) * (x2+1-x1)


part1 = 0
for i in range(len(points)):
    for j in range(i):
        a = area(points[i], points[j])
        part1 = max(a, part1)

print('Part 1:', part1)

from collections import defaultdict
rows = defaultdict(list)
cols = defaultdict(list)
x_values = set()
y_values = set()
for x,y in points:
    rows[y].append(x)
    cols[x].append(y)
    x_values.add(x)
    y_values.add(y)
x_values = sorted(list(x_values))
y_values = sorted(list(y_values))

x_dict = dict()
y_dict = dict()

for i in range(len(x_values)):
    x_dict[x_values[i]] = i*2
for i in range(len(y_values)):
    y_dict[y_values[i]] = i*2

for i in cols.keys():
    cols[i] = sorted(cols[i])
for i in rows.keys():
    rows[i] = sorted(rows[i])


def condense(point):
    x,y = point
#    return x,y
    return x_dict[x], y_dict[y]

condensed_points = [condense(p) for p in points]

@lru_cache(maxsize=None)
def in_shape(point):
    # raycast left
    crossings_left = 0
    crossings_down = 0
#    print('point', point)
    for i in range(len(points)):
        a = condensed_points[i]
        b = condensed_points[i-1]
#        print(a, b)
        if a[0] == b[0]:
            # vertical
            if a[0] <= point[0] and min(a[1], b[1]) < point[1] < max(a[1], b[1]): crossings_left += 1
        else:
            # horizontal
            if a[1] <= point[1] and min(a[0], b[0]) < point[0] < max(a[0], b[0]): crossings_down += 1
#    print(crossings_left, crossings_down)
    if crossings_left % 2 == 0: return False
    if crossings_down % 2 == 0: return False
    return True

# 1887241
# 920948
part2 = 0
for i in range(len(points)):
    if i % 50 == 0:
        print(f'At {i} out of {len(points)}. Best is {part2}')
    for j in range(i):
        a = area(points[i], points[j])
        if a > part2:
            flag = True
            p1 = condensed_points[i]
            p2 = condensed_points[j]
#            print(p1, p2, '@')
            x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
            y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
            for x in range(x1+1, x2, 2):
                for y in range(y1+1, y2, 2):
#                    print((x,y), in_shape((x, y)))
                    if not in_shape((x,y)):
                        flag = False
                        break
                if not flag: break
            if flag:
#                print(p1, p2, '!')
                part2 = a
print('Part 2:', part2)

