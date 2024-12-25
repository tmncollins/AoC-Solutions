from _collections import defaultdict


def get_value(r):
    global wires

    global wires
    try: return int(r)
    except: return wires[r]


with open("inputs/Day7.txt") as f:
    all_data = f.read().split("\n")

WIRE_MAX = 65535
WIRE_MIN = 0
instructions = []
for line in all_data:
    if "->" in line: instructions.append(line.split("->"))

def run():
    global instructions, wires
    wires = defaultdict(int)

    for i in range(100):
        for instruct in instructions:

            cmd, r = instruct
            r = r.strip()
            v = 0

            cmd = cmd.split()
            if len(cmd) == 1:
                v = get_value(cmd[0])
            elif cmd[0] == "NOT":
                v = WIRE_MAX - get_value(cmd[1])
            elif cmd[1] == "AND":
                v = get_value(cmd[0]) & get_value(cmd[2])
            elif cmd[1] == "OR":
                v = get_value(cmd[0]) | get_value(cmd[2])
            elif cmd[1] == "LSHIFT":
                x = get_value(cmd[2])
                v = get_value(cmd[0]) * pow(2, x)
            elif cmd[1] == "RSHIFT":
                x = get_value(cmd[2])
                v = get_value(cmd[0]) // pow(2, x)

            wires[r] = v

    return wires["a"]


part1 = run()
print("Part 1:", part1)

for i in range(len(instructions)):
    if instructions[i][1].strip() == "b":
        instructions[i][0] = str(part1)
        break

print("Part 2:", run())