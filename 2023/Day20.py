from _collections import deque, defaultdict
from copy import deepcopy
from math import gcd

def lcm(a, b):
    return (a*b) // gcd(a,b)

with open("inputs/Day20.txt") as file:
    data = file.read().strip().split("\n")

type = defaultdict(int)
graph = defaultdict(list)
state = dict()

LOW = 0
HIGH = 1

FLIP_FLOP = 1
CONJUNCTION = 2
BROADCASTER = 3

for line in data:
    if len(line) <= 1: break
    node, con = line.strip().split(" -> ")
    con = con.split(", ")
    if node[0] == "%":
        node = node[1:]
        type[node] = FLIP_FLOP # flip-flop
        state[node] = LOW  # off
    elif node[0] == "&":
        node = node[1:]
        type[node] = CONJUNCTION # conjunction
        state[node] = dict()
    else:
        type[node] = BROADCASTER # broadcast
    graph[node] = con

for node in graph:
    for v in graph[node]:
        if type[v] == CONJUNCTION:
            state[v][node] = LOW

STATE_RESET = deepcopy(state)

def run():
    global state, graph, type, part2

    process = deque()
    counter = {LOW:0, HIGH:0}

    process.append(("broadcaster", LOW, "button"))

    while process:
        node, pulse, last = process.popleft()
        counter[int(pulse)] += 1

        if node == "rx" and pulse == LOW:
            part2 = True
            return

        if type[node] == FLIP_FLOP:
            if pulse == HIGH:
                continue
            state[node] = not state[node]
            for v in graph[node]:
                process.append((v, state[node], node))

        elif type[node] == CONJUNCTION:
            state[node][last] = int(pulse)
            if LOW in state[node].values():
                for v in graph[node]:
                    process.append((v, HIGH, node))
            else:
                for v in graph[node]:
                    process.append((v, LOW, node))

        else:
            for v in graph[node]:
                process.append((v, pulse, node))

    return counter

counter = {LOW: 0, HIGH: 0}
for i in range(1000):
    c = run()
    counter[LOW] += c[LOW]
    counter[HIGH] += c[HIGH]

print("Part 1:", counter[LOW]*counter[HIGH])

state = deepcopy(STATE_RESET)
vals = []

for i in graph["broadcaster"]:
    j = i
    number = ""
    while True:
#        print(j, graph[j])
        if len(graph[j]) == 2:
            number += "1"
            if type[graph[j][0]] == CONJUNCTION:
                j = graph[j][1]
            else:
                j = graph[j][0]
        else:
            j = graph[j][0]
            if type[j] == CONJUNCTION:
                number += "1"
                break
            number += "0"
    number = number[::-1]
    n = int(number, 2)
    vals.append(n)

while len(vals) > 1:
    a = vals.pop()
    b = vals.pop()
    vals.append(lcm(a, b))

print("Part 2:", vals[0])