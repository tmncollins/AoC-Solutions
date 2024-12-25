import heapq
from _collections import deque, defaultdict

keypad = {"^":[("v", "v"), (">", "A")], "A":[("<", "^"), ("v", ">")], "<":[(">", "v")],
          "v":[("<", "<"), (">", ">"), ("^", "^")], ">":[("<", "v"), ("^", "A")]}
buttons = "Av<>^"

number_pad = defaultdict(list)
for i in range(1, 10):
    if i < 7: number_pad[str(i)].append(("^", str(i+3)))
    if i > 3: number_pad[str(i)].append(("v", str(i-3)))
    if i % 3 != 1: number_pad[str(i)].append(("<", str(i-1)))
    if i % 3 != 0: number_pad[str(i)].append((">", str(i+1)))
number_pad["2"].append(("v", "0"))
number_pad["3"].append(("v", "A"))
number_pad["0"] = [("^", "2"), (">", "A")]
number_pad["A"] = [("^", "3"), ("<", "0")]



codes = """839A
169A
579A
670A
638A""".split("\n")

def generate_keypad(costs):
    new_costs = dict()
    for start in buttons:
        for end in buttons:
            if start == end:
                new_costs[(start, end)] = costs[("A", "A")]
                continue
            seen = dict()
            q = [(0, start, "A")]
            seen[(start, "A")] = 0
            while q:
                d, u, last = heapq.heappop(q)
                if u == end:
                    d2 = d + costs[(last, "A")]
#                    if ("!", "A") not in seen or seen[("!", "A")] >= d2:
                    if (start, end) not in new_costs:
                        new_costs[(start, end)] = d + costs[(last, "A")]
                    else:
                        new_costs[(start, end)] = min(new_costs[(start, end)], d + costs[(last, "A")])
                    continue
                for m, v in keypad[u]:
                    d2 = d + costs[(last, m)]
                    if (v, m) not in seen or seen[(v,m)] >= d2:
                        seen[(v,m)] = d2
                        heapq.heappush(q, (d2, v, m))
    return new_costs

def input_code(code, costs):
    q = [(0, 0, "A", "A")]
    seen = dict()
    seen[(0,"A","A")] = 0
    while q:
        d, i, u, last = heapq.heappop(q)
#        print(d, i, u, last)
        if i == 4: return d
        if code[i] == u:
            d2 = d + costs[(last, "A")]
            if (i+1, u, "A") not in seen or seen[(i+1, u, "A")] >= d2:
                seen[(i+1, u, "A")] = d2
                heapq.heappush(q, (d2, i+1, u, "A"))
#            continue
        for m, v in number_pad[u]:
            d2 = d + costs[(last, m)]
#            print(m, v, d2)
            if (i, v, m) not in seen or seen[(i, v, m)] >= d2:
                seen[(i, v, m)] = d2
                heapq.heappush(q, (d2, i, v, m))

initial_costs = dict()
for a in buttons:
    for b in buttons:
        initial_costs[(a,b)] = 1

costs = dict(initial_costs)
for _ in range(2):
    costs = generate_keypad(costs)
costs2 = dict(costs)
for _ in range(23):
    costs2 = generate_keypad(costs2)

part1 = 0
part2 = 0
for code in codes:
    c = int(code.replace("A", ""))
    ic = input_code(code, costs)
    ic2 = input_code(code, costs2)
    part1 += c * ic
    part2 += c * ic2
print("Part 1:", part1)
print("Part 2:", part2)

# 296075832163520
# 252473394928452
# 258508644029692