def get_dist(run_time, reindeer):
    name, speed, time, rest = reindeer
    dist = 0

    while run_time >= 0:
        t = min(time, run_time)
        dist += speed * t
        run_time -= t
        run_time -= rest

    return dist


with open("inputs/Day14.txt") as f:
    data = f.read().split("\n")

reindeer = []

for line in data:
    if len(line) < 5: continue

    line = line.split()
    name = line[0]
    speed = int(line[3])
    time = int(line[6])
    rest = int(line[-2])
    reindeer.append([name, speed, time, rest])

run_time = 2503
distances = []

for r in reindeer:
    d = get_dist(run_time, r)
    distances.append((d, r[0]))

distances.sort()
print("Part 1:", distances[-1][0])

distances = [[0, r[1], r[2], r] for r in reindeer]
scores = {r[0]:0 for r in reindeer}

for i in range(run_time):

    for j in range(len(distances)):
        d, v, t, r = distances[j]
        d += v
        t -= 1
        if t == 0:
            if v == 0:
                v = r[1]
                t = r[2]
            else:
                v = 0
                t = r[3]
        distances[j] = [d,v,t,r]

    distances.sort()
    winning_distance = distances[-1][0]
    for j in range(len(distances)):
        if distances[j][0] == winning_distance:
            winner = distances[j][3][0]
            scores[winner] += 1

print("Part 2:", max(scores.values()))