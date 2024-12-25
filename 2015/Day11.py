pzl_inp = input("Enter puzzle input:    ").strip()

alpha = "abcdefghijklmnopqrstuvwxyz"
password = []
for c in pzl_inp: password.append(alpha.index(c))


def output():
    global password
    s = ""
    for p in password: s += alpha[p]
    print(s)


def valid():
    global password
    banned = {8, 14, 11}

    straight = False
    for i in range(len(password) - 2):
        if password[i] + 1 == password[i+1] and password[i] + 2 == password[i+2]:
            straight = True
            break

    if not straight:
        return False

    doubles = set()
    if password[-1] in banned: return False
    for i in range(len(password) - 1):
        if password[i] in banned: return False
        if password[i] == password[i+1]:
            doubles.add(password[i])

    return len(doubles) >= 2


def inc(p=-1):
    global password

    password[p] += 1
    if password[p] == 26:
        password[p] = 0
        inc(p-1)


while not valid():
    inc()
print("Part 1:", end=" ")
output()

inc()
while not valid():
    inc()
print("Part 2:", end=" ")
output()
