with open('inputs/19 - 1.txt', 'r') as f: #open the file
    r = f.readlines()
with open('inputs/19 - 2.txt', 'r') as f: #open the file
    words = f.readlines()


from _collections import defaultdict
rules = defaultdict(list)

def split(a):
    return a.split()

for line in r:
    line = line.split(": ")
    if "\"" in line[1]:
        rules[line[0]] = line[1]
    else:
        right = list(map(split, line[1].split("|")))
        rules[line[0]] = right

def valid(string, rule):
    if len(string) == 0: return False, string
    if "\"" in rules[rule]:
        return string[0] == rules[rule][1], string[1:]
    for option in rules[rule]:
        s = string
        va = True
        for match in option:
            v,s = valid(s, match)
            if not v:
                va = False
                break
        if va:
            return True, s
    return False, string

tot = 0
for line in words:
    line = line.replace("\n", "")
    v, s= valid(line, "0")
    if v and s == "": tot += 1

print(tot)

