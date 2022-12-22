
nums = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
alpha = "abcdefg"
data = open("inputs/Day8.txt").read().split("\n")

count = 0
tot = 0

def setdig(a, s, digits):
    for b in alpha:
        if b in a:
            if len(s) == 1:
                digits[b] = list(s)[0]
            else:
                digits[b] = s
        else:
            for item in s:
                if item in digits[b]:
                    digits[b].remove(item)

for entry in data:
    ex, output = entry.split("|")
    ex = ex.split()
    digits = dict()

    for a in alpha: digits[a] = set(alpha)

    # find 1 and 7
    for i in range(len(ex)):
        ex[i] = [len(ex[i]), set(ex[i])]
    ex = sorted(ex)
    # pos 0 is 1, pos 1 is 7, pos 2 is 4
    for a in nums[1]:
        digits[a] = set(ex[0][1])
    A = ex[1][1].difference(ex[0][1])
    setdig("a", A, digits)
    BD = ex[2][1].difference(ex[0][1])
    setdig("bd", BD, digits)
    EG = ex[-1][1].difference(ex[2][1])
    EG.remove(digits["a"])
    setdig("eg", EG, digits)

    # more gs than es
    # more fs than cs
    # more ds than bs
    E = list(EG)[0]
    G = list(EG)[1]
    B = list(BD)[0]
    D = list(BD)[1]
    CF = list(digits["c"])
    C = CF[0]
    F = CF[1]
    ce, cg = 0, 0
    cb, cd = 0, 0
    cc, cf = 0, 0
    for l, item in ex:
        if E in item: ce += 1
        if G in item: cg += 1
        if B in item: cb += 1
        if C in item: cc += 1
        if F in item: cf += 1
        if D in item: cd += 1
    if cg > ce:
        digits["g"] = G
        digits["e"] = E
    else:
        digits["e"] = G
        digits["g"] = E
    if cd > cb:
        digits["d"] = D
        digits["b"] = B
    else:
        digits["d"] = B
        digits["b"] = D
    if cf > cc:
        digits["f"] = F
        digits["c"] = C
    else:
        digits["f"] = C
        digits["c"] = F

    revdigits = dict()
    for a in alpha:
        revdigits[digits[a]] = a

#    print(digits)
    output = output.split()
#    print(revdigits)
    num = ""
    for item in output:
        if len(item) in [2,3,4,7]: count += 1
        for a in alpha:
            if a in item:
                item = item.replace(a, revdigits[a].upper())
        item = "".join(sorted(item)).lower()
        num += str(nums.index(item))

    tot += int(num)


print("Part 1:", count)
print("Part 2:", tot)

