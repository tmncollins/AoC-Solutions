from _collections import *

with open("inputs/25.txt") as f:
    all_data = f.read().split("\n")

states = dict()
tape = defaultdict(int)
state = ""

curr_state = [[0,0,""], [0,0,""]]
curr_val = -1
curr_state_name = ""
steps = 0

for line in all_data:
    line = line.strip()
    if len(line) < 5: continue
    line = line.split()

    if line[0] == "Begin":
        state = line[3].replace(".", "")
    elif line[0] == "Perform":
        steps = int(line[5])
    elif line[0] == "In":
        states[curr_state_name] = curr_state
        curr_state = [[0,0,0], [0,0,0]]
        curr_state_name = line[2].replace(":", "")
    elif line[0] == "If":
        curr_val = int(line[5].replace(":", ""))
    elif line[0] == "-":

        if line[1] == "Write":
            curr_state[curr_val][0] = int(line[4].replace(".", ""))
        elif line[1] == "Move":
            if line[6] == "right.":
                curr_state[curr_val][1] = 1
            elif line[6] == "left.":
                curr_state[curr_val][1] = -1
        elif line[1] == "Continue":
            curr_state[curr_val][2] = line[4].replace(".", "")

states[curr_state_name] = curr_state

ptr = 0
for i in range(steps):
    if i % 1000000 == 0: print(i, "out of", steps)
    s = states[state][tape[ptr]]
    tape[ptr] = s[0]
    ptr += s[1]
    state = s[2]

print("Part 1:", sum(tape.values()))