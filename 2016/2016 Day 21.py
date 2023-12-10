with open("inputs/Day21.txt") as f:
    contents = f.read().split("\n")

string = ""

def rotate(n):
    global string
    n = n % len(string)
    for i in range(n):
        a = string.pop()
        string.insert(0,a)

def process(instruct):
    global string
    instruct = instruct.split()
    if instruct[0] == "swap":
        if instruct[1] == "position":
            a = string[int(instruct[2])]
            b = string[int(instruct[5])]
            string[int(instruct[5])] = a
            string[int(instruct[2])] = b
        else:
            a = string.index(instruct[2])
            b = string.index(instruct[5])
            string[a] = instruct[5]
            string[b] = instruct[2]
    elif instruct[0] == "rotate":
        if instruct[1] == "left":
            rotate(len(string) - int(instruct[2]))
        elif instruct[1] == "right":
            rotate(int(instruct[2]))
        else:
            a = string.index(instruct[6])
            if a >= 4: a += 1
            rotate(1 + a)
    elif instruct[0] == "reverse":
        a  = int(instruct[2])
        b = int(instruct[4])
        string = string[:a] + string[a:b+1][::-1] + string[b+1:]
    elif instruct[0] == "move":
        a = string.pop(int(instruct[2]))
        string.insert(int(instruct[5]), a)

unrot = {1:1, 3:2, 5:3, 7:4, 2:6, 4:7, 6:8, 0:9}
def unprocess(instruct):
    global string
    instruct = instruct.split()
    if instruct[0] == "swap":
        process(" ".join(instruct))
    elif instruct[0] == "rotate":
        if instruct[1] == "left":
            instruct[1] = "right"
            process(" ".join(instruct))
        elif instruct[1] == "right":
            instruct[1] = "left"
            process(" ".join(instruct))
        else:
            p = string.index(instruct[6])
            d = unrot[p]
            process("rotate left " + str(d) + " step")
    elif instruct[0] == "reverse":
        process(" ".join(instruct))
    elif instruct[0] == "move":
        a = instruct[2]
        instruct[2] = instruct[5]
        instruct[5] = a
        process(" ".join(instruct))


def part1(s):
    global string
    string = list(s)
    for line in contents:
        process(line)
    print("Part 1:", "".join(string))

def part2(s):
    global string
    string = list(s)
    for line in contents[::-1]:
        unprocess(line)
    print("Part 2:", "".join(string))

part1("abcdefgh")
part2("fbgdceah")

"""

"""
