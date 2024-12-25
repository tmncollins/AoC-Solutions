def operand(i):
    global reg
    if i <= 3: return i
    return reg[i-4]

def opcode(code, value):
    global reg, idx, out
    if code == 0:
        reg[0] = int(reg[0] // (2**value))
    elif code == 1:
        reg[1] = (reg[1] ^ value)
    elif code == 2:
        reg[1] = (value % 8)
    elif code == 3:
        if reg[0] > 0:
            idx = value - 2
    elif code == 4:
        reg[1] = (reg[1]^reg[2])
    elif code == 5:
        out.append(str(value%8))
    elif code == 6:
        reg[1] = int(reg[0] // (2**value))
    elif code == 7:
        reg[2] = int(reg[0] // (2**value))

def run(program):
    global reg, idx, out
    out = []
    idx = 0
    while idx >= 0 and idx+1 < len(program):
        opcode(program[idx], operand(program[idx+1]))
        idx += 2
    return ",".join(out)

def cycle():
    global reg,out
    reg[1] = reg[0] % 8
    reg[1] = reg[1] ^ 2
    reg[2] = reg[0] // (2**reg[1])
    reg[1] = reg[1] ^ reg[2]
    reg[1] = reg[1] ^ 3
    out.append(reg[1]%8)
    reg[0] //= 8
    return reg[0]

def run2():
    global out, idx
    out = []
    x = cycle()
    while x:
        x = cycle()

reg = [2024,0,0]
program_string = "2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0"
#program_string = "0,3,5,4,3,0"
program = list(map(int, program_string.split(",")))
out = run(program)
print(out)


p = 15
options = [0]
x = 1
while p >= 0:
    new_options = []
    for i in range(8):
        for item in options:
            A = item * 8 + i
            reg = [A,0,0]
            run2()
            if out[:x] == program[-x:]:
                new_options.append(A)
    options = new_options

    p -= 1
    x += 1

part2 = min(options)
reg = [part2, 0, 0]
out = run(program)
print(out)
print(min(options), len(options))



