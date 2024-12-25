"""
The circuit should represent the following adder:
X XOR Y -> A
X AND Y -> B
A XOR Carry -> Z
B AND Carry -> C
B OR C -> Carry
"""

from _collections import deque

def process(a, b, op):
    global values
    a, b = values[a], values[b]
    if op == "OR": return a | b
    elif op == "XOR": return a ^ b
    elif op == "AND": return a & b
    return 0

all_data = open("inputs/Day24.txt").read().split("\n")
values = dict()
to_do = deque()
highest_bit = "z00"
for line in all_data:
    if "->" in line:
        line = line.split()
        to_do.append([line[0], line[1], line[2], line[4]])
        if line[4][0] == "z": highest_bit = max(highest_bit, line[4])
    elif ":" in line:
        line = line.split(": ")
        values[line[0]] = int(line[1])

to_swap = set()
for a, op, b, out in to_do:
    if out[0] == "z" and op != "XOR" and out != highest_bit:
        to_swap.add(out) # output bits should always be XOR
    elif op == "XOR" and out[0] != "z" and a[0] not in "xy" and b[0] not in "xy":
        to_swap.add(out) # XOR may only be used on the input bits or to give an output bit
    if op == "AND" and a != "x00" and b != "x00":
        for c, op2, d, out2 in to_do:
            if (out == c or out == d) and op2 != "OR":
                # AND is only used to handle carrying. It should then be ORed with the other carry component
                to_swap.add(out)
                break
    if op == "XOR":
        for c, op2, d, out2 in to_do:
            if (out == c or out == d) and op2 == "OR":
                # XOR is only used to handle outputting. It should be ORed with a carry component
                to_swap.add(out)
                break

while to_do:
    a, op, b, out = to_do.popleft()
    if a in values and b in values: values[out] = process(a, b, op)
    else: to_do.append([a,b,op,out])

binary = ""
for i in range(int(highest_bit[1:])+1):
    i_str = str(i)
    if len(i_str) < 2: i_str = "0" + i_str
    i_str = "z" + i_str
    if i_str in values: binary = str(values[i_str]) + binary

print("Part 1:", int(binary, 2))
to_swap = sorted(list(to_swap))
part2 = ",".join(to_swap)
print("Part 2:", part2)