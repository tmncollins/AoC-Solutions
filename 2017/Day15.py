A = 703
B = 516

def part1(A, B):
    judge = 0
    x = pow(2, 16)
    for i in range(40000000):
        if i % 100000 == 0: print(i)
        A *= 16807
        A %= 2147483647
        B *= 48271
        B %= 2147483647

    #    a = bin(A)[-16:]
    #    b = bin(B)[-16:]
        if (A % x) == (B % x):
    #    if a == b:
            judge += 1

    print("Part 1:", judge)

def part2(A, B):
    judge = 0
    x = pow(2, 16)
    for i in range(5000000):
        if i % 100000 == 0: print(i)
        A *= 16807
        A %= 2147483647
        while A % 4 != 0:
            A *= 16807
            A %= 2147483647
        B *= 48271
        B %= 2147483647
        while B % 8 != 0:
            B *= 48271
            B %= 2147483647

        #    a = bin(A)[-16:]
        #    b = bin(B)[-16:]
        if (A % x) == (B % x):
            #    if a == b:
            judge += 1

    print("Part 2:", judge)

print(part2(A, B))