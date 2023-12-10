from _collections import deque

def highestBit(n):
    i = 0
    while True:
        if 2**i == n: return 2**i
        elif 2**i > n: return 2**(i-1)
        i += 1

def solve(n):
    l = n - highestBit(n)
    print("Part 1:", ((2 * l + 1)%n))

def part2(n):
    winner = 1
    for i in range(3,n+1):
        dead = (i // 2) + 1
        winner += 1
        if winner >= dead: winner += 1
        if winner > i: winner -= i
#        print(winner)
    print("Part 2:", winner)

n = int(input("Enter puzzle input:    "))
solve(n)
part2(n)
