def snafu_to_dec(i):
    i = i[::-1]
    conv = {"1":1, "2":2, "0":0, "-":-1, "=":-2}

    num = 0
    for j in range(len(i)):
        f = pow(5, j)
        num += f * conv[i[j]]

    return num

def dec_to_snafu(i):

    snafu = []

    p = 1
    while p < i:
        p *= 5

    while p > 0:
        snafu.append(i // p)
        i = i % p
        p //= 5

    print(snafu)

    for j in range(len(snafu)-1, -1, -1):
        if snafu[j] == 3:
            snafu[j] = -2
            snafu[j-1] += 1
        if snafu[j] == 4:
            snafu[j] = -1
            snafu[j-1] += 1
        if snafu[j] == 5:
            snafu[j] = 0
            snafu[j-1] += 1

    print(snafu)

    conv = {2:"2", 1:"1", 0:"0", -1:"-", -2:"="}

    while snafu[0] == 0: snafu.pop(0)

    num = ""
    for item in snafu:
        num += conv[item]

    return num


with open("inputs/Day25.txt") as f:
    data = f.read().strip().split("\n")

tot = 0
for item in data:
    x = snafu_to_dec(item)
    print(item, x)
    tot += x

print(tot)
print(dec_to_snafu(tot))