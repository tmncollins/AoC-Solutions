with open("inputs/Day7.txt") as f:
    all_data = f.read().split("\n")


def abba(s):

    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True

    return False


def tls(ip):
    ip = "X" + ip
    ip = ip.replace("]", "[").split("[")

    valid = False
    for i in range(len(ip)):
        if abba(ip[i]):
            if i % 2 == 0:
                valid = True
            else:
                return False

    return valid


def aba(s):
    ret = []
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            ret.append(s[i:i+3])
    return ret


def bab(s, a):
    b = a[1] + a[0] + a[1]
    return b in s


def ssl(ip):
    ip = "X" + ip
    ip = ip.replace("]", "[").split("[")
    sqr = []
    not_sqr = []
    abas = []

    for i in range(len(ip)):
        if i % 2 == 0:
            not_sqr.append(ip[i])
        else:
            sqr.append(ip[i])

    for line in not_sqr:
        ABA = aba(line)
        for item in ABA:
            abas.append(item)

    for line in sqr:
        for a in abas:
            if bab(line, a):
                return True

    return False


part1 = 0
part2 = 0

for line in all_data:
    if len(line) < 5: continue
    if tls(line):
        part1 += 1
    if ssl(line):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
