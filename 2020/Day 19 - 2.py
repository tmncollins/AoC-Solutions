with open('inputs/19 - 1.txt', 'r') as f: #open the file
    r = f.readlines()
with open('inputs/19 - 2.txt', 'r') as f: #open the file
    words = f.readlines()


from _collections import defaultdict
rules = defaultdict(list)

def split(a):
    return a.split()

r.append("8: 42 | 42 8")
r.append("11: 42 31 | 42 11 31")
#r.append("99: 8")
#r.append("98: 11")

for line in r:
    line = line.split(": ")
    if "\"" in line[1]:
        rules[line[0]] = [[line[1].replace("\n", "")]]
    else:
        right = list(map(split, line[1].split("|")))
        rules[line[0]] = right

import re

def parse(lines):
    it = iter(lines)
    rules = {}
    while (line := next(it).rstrip()):
        lhs, rhs = line.split(':', maxsplit=1)
        rules[lhs] = [branch.split() for branch in rhs.split('|')]
    return rules

def regexPattern(rule):
    start = "(?:"
    end = ")"

    bigReg = []
    for option in rules[rule]:
#        print(option)
        relist = [i[1:-1] if len(i) > 2 and i[0] == i[-1] == "\"" else
                  regexPattern(i) for i in option]
        bigReg.append(relist)

    regex = "|".join(["".join(item) for item in bigReg])

    return start + regex + end

maxLen = 0
for item in words:
    if len(item) > maxLen: maxLen = len(item)

tot = 0

rules = parse(r + [""])

regex31 = regexPattern("31")
regex42 = regexPattern("42")

regex8 = "(?:" + regex42 + ")+"
regex11 = "|".join(["(?:" + regex42 + "){" + str(i) + "}(?:" + regex31 + "){" + str(i) + "}" for i in range(1, (maxLen + 2) // 2)])

regex0 = re.compile("(?:" + regex8 + "){1}" + "(?:" + regex11 + "){1}")

tot = 0

for item in words:
    if regex0.fullmatch(item.rstrip()): tot += 1

print(tot)