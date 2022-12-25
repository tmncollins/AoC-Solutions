from _collections import defaultdict

with open("inputs/Day21.txt") as f:
    all_data = f.read().split("\n")

values = dict()

def get_monkey(a):
    if len(values[a]) == 1:
        return values[a][0]
    else:
        x = get_monkey(values[a][0])
        y = get_monkey(values[a][2])
        op = values[a][1]
        if op == "+":
            return x+y
        elif op == "-":
            return x-y
        elif op == "*":
            return x*y
        elif op == "/":
            return x/y


def equal(hmn):
    values["humn"] = [hmn]
    x = get_monkey(values["root"][0])
    y = get_monkey(values["root"][2])
    print(x, y)
    return x == y


for line in all_data:
    if len(line) < 5: continue

    r, line = line.split(":")
    line = line.split()

    if len(line) == 1:
        values[r] = [int(line[0])]

    else:
        values[r] = line

print("Part 1:", int(get_monkey("root")))

########## PART 2 ##########

def contain_humn(monkey):
    if monkey == "humn": return True
    if len(values[monkey]) == 1:
        return False
    else:
        return contain_humn(values[monkey][0]) or contain_humn(values[monkey][2])


def monkey_to_string(a):
    if len(values[a]) == 1:
        return str(values[a][0])
    else:
        x = monkey_to_string(values[a][0])
        y = monkey_to_string(values[a][2])
        op = values[a][1]
        eq = "(" + x + op + y + ")"
        try:
            return str(int(eval(eq)))
        except:
            return eq

values["humn"] = "x"

# get the two values passed to root
left = monkey_to_string(values["root"][0])
right = monkey_to_string(values["root"][2])

# get the num one
num = 0
unknown = ""
try:
    num = int(left)
    unknown = right
except:
    num = int(right)
    unknown = left

ops = "+-/*"
while unknown != "x":
    # remove outer brackets
    unknown = unknown[1:-1]
    op = ""
    x_left = False
    op_val = 0
    for i in range(len(unknown)):
        if unknown[i] == "(": break
        elif unknown[i] in ops:
            op = unknown[i]
            try:
                op_val = int(unknown[:i])
                unknown = unknown[i+1:]
            except:
                op = ""
            break
    if op == "":
        for i in range(len(unknown)-1, -1, -1):
            if unknown[i] == ")":
                break
            elif unknown[i] in ops:
                op = unknown[i]
                op_val = int(unknown[i+1:])
                unknown = unknown[:i]
                x_left = True
                break

    if op != "":
        if op == "*":
            num /= op_val
        elif op == "/":
            if x_left:
                num *= op_val
            else:
                num = op_val / num
        elif op == "+":
            num -= op_val
        elif op == "-":
            if x_left:
                num += op_val
            else:
                num = op_val - num

print("Part 2:", int(num))
