with open('inputs/8.txt', 'r') as f: #open the file
    contents = f.readlines()

def test(contents):
    acc = 0
    seen = set()
    index = 0
    loop = True
    while index not in seen:
        if index >= len(contents):
            loop = False
            break
        seen.add(index)
        line = contents[index].split()
        if line[0] == "acc":
            p = line[1][0]
            if p == "+":
                acc += int(line[1][1:])
            else:
                acc -= int(line[1][1:])
            index += 1
        elif line[0] == "jmp":
            p = line[1][0]
            if p == "+":
                index += int(line[1][1:])
            else:
                index -= int(line[1][1:])
        else:
            index += 1

    if not loop:
        print(acc)

for i in range(len(contents)):
    if contents[i].split()[0] == "nop":
        c = list(contents)
        c[i] = c[i].replace("nop", "jmp")
        test(c)
    elif contents[i].split()[0] == "jmp":
        c = list(contents)
        c[i] = c[i].replace("jmp", "nop")
        test(c)

        