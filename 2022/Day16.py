from _collections import *
from heapq import *
from itertools import *
import time as Time


with open("inputs/Day16.txt") as f:
    all_data = f.read().split("\n")

graph = defaultdict(set)
flow_rate = defaultdict(int)
start = Time.time()

for line in all_data:
    if len(line) < 10: continue
    flow, move = line.split(";")
    move = move.replace("tunnel", "").replace("s", "").replace("lead", "").replace("valve", "").replace("to", "").strip().split(",")
    flow = flow.replace("Valve", "").replace("has flow rate", "").strip().split("=")

    u = flow[0].strip()
    rate = int(flow[1])
    flow_rate[u] = rate
    for v in move:
        v = v.strip()
        graph[u].add(v)

q = [(0, 30, "AA", set())]
seen = defaultdict(int)
seen = set()

flow_valves = set()
for valve in flow_rate:
    if flow_rate[valve] > 0:
        flow_valves.add(valve)

flow_valves_dist = defaultdict(int)
check_valves = set(flow_valves)
check_valves.add("AA")

for valve in check_valves:
    q = deque([(0, valve)])
    seen = {valve}

    while q:
        d, u = q.popleft()
        if u in flow_valves:
            flow_valves_dist[(valve, u)] = d

        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append((d+1, v))

q = [(0, 30, "AA", set())]
q = deque(q)
max_pressure = 0

while q:
    pressure, time, u, seen = q.popleft()
#    print(pressure, time, u, seen)

    max_pressure = max(pressure, max_pressure)

    for v in flow_valves:
        if v not in seen:
            time2 = time-1-flow_valves_dist[(u, v)]
            if time2 >= 0:
                pressure2 = time2 * flow_rate[v] + pressure
                seen2 = set(seen)
                seen2.add(v)
                q.append((pressure2, time2, v, seen2))

print("Part 1:", max_pressure)

q = [(0, 26, "AA", set())]
q = deque(q)
max_pressure = 0

visits = defaultdict(int)

while q:
    pressure, time, u, seen = q.popleft()

    s = "-".join(sorted(seen))
    if visits[s] < pressure:
        visits[s] = pressure

    for v in flow_valves:
        if v not in seen:
            # move and open
            time2 = time-1-flow_valves_dist[(u, v)]
            if time2 >= 0:
                pressure2 = time2 * flow_rate[v] + pressure
                seen2 = set(seen)
                seen2.add(v)
                q.append((pressure2, time2, v, seen2))

keys = list(visits.keys())
max_pressure = 0
for a in range(len(keys)):
    key_a = set(keys[a].split("-"))
#    print(visits[keys[a]])
    for b in range(a):
        key_b = keys[b].split("-")

#        print(key_a, key_b)

        intersect = False
        for item in key_b:
            if item in key_a:
                intersect = True
                break
        if intersect: continue

#        print(visits[keys[a]] + visits[keys[b]], visits[keys[a]], visits[keys[b]])
        max_pressure = max(max_pressure, visits[keys[a]] + visits[keys[b]])

print("Part 2:", max_pressure)
# elephant : DD HH EE
# me       : JJ BB CC





