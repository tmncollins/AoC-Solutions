pre = 26
with open('inputs/9.txt', 'r') as f: #open the file
    contents = list(map(int, f.readlines()))

def p1(contents):
    i = 26
    while True:
        valid  = False
        for j in range(i-26, i):
            if contents[i] - contents[j] in contents[i-26: i]:
                valid = True
                break
        if not valid:
            return contents[i]
        i += 1

print(p1(contents))