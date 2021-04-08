with open('inputs/8.txt', 'r') as f: #open the file
    contents = f.readlines()

acc = 0
seen = set()
index = 0
while index not in seen:
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

print(acc)
