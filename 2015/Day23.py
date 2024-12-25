with open("inputs/Day23.txt") as f:
    all_data = f.read().split("\n")

instructions = []

for line in all_data:
    if len(line) < 3: continue

    line = line.replace(",", "").replace("+", "").split()
    instructions.append(line)


def run(a, b):
    reg = {"a": a, "b": b}
    ptr = 0

    while ptr >= 0 and ptr < len(instructions):
        cmd = instructions[ptr]

        if cmd[0] == "hlf":
            reg[cmd[1]] //= 2
        elif cmd[0] == "tpl":
            reg[cmd[1]] *= 3
        elif cmd[0] == "inc":
            reg[cmd[1]] += 1
        elif cmd[0] == "jmp":
            ptr += int(cmd[1]) - 1
        elif cmd[0] == "jie":
            if reg[cmd[1]] % 2 == 0:
                ptr += int(cmd[2]) - 1
        elif cmd[0] == "jio":
            if reg[cmd[1]] == 1:
                ptr += int(cmd[2]) - 1

        ptr += 1

    return reg["a"], reg["b"]


print("Part 1:", run(0, 0)[1])
print("Part 2:", run(1, 0)[1])
