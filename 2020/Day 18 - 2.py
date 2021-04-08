with open('inputs/18.txt', 'r') as f: #open the file
    homework = f.readlines()

ops = ["*", "+"]


def process(v):
    curr = int(v[0])
    op = ""
    if "+" in v:
        next = [str(curr)]
        for i in range(1,len(v)):
            if v[i] in ops:
                op = v[i]
                next.append(op)
            else:
                if op == "+":
                    next.pop()
                    val = int(next.pop())
                    val += int(v[i])
                    next.append(str(val))
                else: next.append(v[i])
        return process(next)
    else:
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


#print(evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2".replace("(", "( ").replace(")", " )").replace("\n", "")))

#input()
tot = 0
for line in homework:
    tot += evaluate(line.replace("(", "( ").replace(")", " )").replace("\n", ""))

print(tot)
