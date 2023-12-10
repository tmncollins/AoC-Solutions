from collections import defaultdict

with open("inputs/Day12.txt") as f:
    instructions = f.read().split("\n")

def part1(register):

    ind = 0
    while ind < len(instructions):
        instruct = instructions[ind].split()
#        print(instruct)
        if instruct[0] == "cpy":
            try:
                a = int(instruct[1])
                register[instruct[2]] = a
            except:
                register[instruct[2]] = register[instruct[1]]
        elif instruct[0] == "inc":
            register[instruct[1]] += 1
        elif instruct[0] == "dec":
            register[instruct[1]] -= 1
        elif instruct[0] == "jnz":
            try:
                a = int(instruct[1])
                if a != 0:
                    ind += int(instruct[2]) - 1
            except:
                if register[instruct[1]] != 0:
                    ind += int(instruct[2]) - 1

        ind += 1

    return register["a"]


r = defaultdict(int)
print("Part 1:", part1(r))

r = defaultdict(int)
r["c"] = 1
print("Part 2:", part1(r))
