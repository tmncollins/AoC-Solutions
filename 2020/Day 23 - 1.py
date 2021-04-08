cups = list(map(int, list("193467258")))
#cups = list(map(int, list("389125467")))


curr = 0

for _ in range(100):
    print(cups)
    n = cups[curr]-1
    N = cups[curr]
    a = []
    for i in range(3):
        if curr + 1 >= len(cups):
            a += [cups.pop(0)]
        else:
            a += [cups.pop(curr+1)]
    while n not in cups:
        n = (n-1)%10
    n = cups.index(n)
    for item in a[::-1]:
        cups.insert(n+1,item)
    curr = cups.index(N)
    curr = (curr+1) % len(cups)

print("".join(list(map(str,cups))))





