with open('inputs/18.txt', 'r') as f: #open the file
    homework = f.readlines()

ops = ["*", "+"]


def process(v):
    curr = int(v[0])
    op = ""
    for i in range(1,len(v)):
        if v[i] in ops: op = v[i]
        else:
            if op == "+": curr += int(v[i])
            elif op == "*": curr *= int(v[i])
    return curr


def evaluate(exp):
    next = []
    curr = []
    operator = ""
    length = 0
    start = 0
    exp = exp.split(" ")
    for i in range(len(exp)):
        item = exp[i]
        if item in ops:
            curr.append(item)
        elif item == "(":
            curr = []
            start = i
        elif item == ")":
            v = process(exp[start+1: i])
            return evaluate(" ".join(exp[:start] + [str(v)] + exp[i+1:]))

            """
            if length <= 1:
                next.pop()
            if curr > 0:
                next.append(str(curr))
            if length > 1:
                next.append(")")
            next.append(operator)
            operator = ""
            curr = 0
            """
        elif item.isnumeric():
            curr.append(item)
    return process(exp)


#print(evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))".replace("(", "( ").replace(")", " )").replace("\n", "")))

#input()
tot = 0
for line in homework:
    tot += evaluate(line.replace("(", "( ").replace(")", " )").replace("\n", ""))

print(tot)
