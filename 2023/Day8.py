from math import gcd

with open("inputs/Day8.txt") as file:
    data = file.read().strip().split("\n")

instructions = ""
graph = dict()
node_a = []
node_z = []
for line in data:
    if len(line) < 3: continue
    if "=" in line:
        line = line.replace("(", "").replace(")", "").replace(",", "").split()
        graph[line[0]] = [line[2], line[3]]
        if line[0][-1] == "A": node_a.append(line[0])
        elif line[0][-1] == "Z": node_z.append(line[0])
    else:
        instructions = line.strip()

node = "AAA"
end = "ZZZ"
steps = 0

def get_steps(node, ends):
    steps = 0
    while node not in ends:
        i = instructions[steps % len(instructions)]
        if i == "L": node = graph[node][0]
        else: node = graph[node][1]
        steps += 1
    return steps

def lcm(a, b):
    return (a * b) // gcd(a, b)

#print("Part 1:", get_steps("AAA", {"ZZZ"}))
part2 = []
for i in node_a:
    part2.append(get_steps(i, set(node_z)))

while len(part2) > 1:
    part2.append(lcm(part2.pop(), part2.pop()))

print(part2[0])