def pow_mod(x, e, mod):
    if e == 1:
        return x

    if e % 2 == 0:
        return (pow_mod(x, e//2, mod) ** 2) % mod

    else:
        return (pow_mod(x, e-1, mod) * x) % mod


with open("inputs/Day25.txt") as f:
    data = f.read().strip().replace(",", "").replace(".", "").split()
    row = int(data[15])
    col = int(data[17])

code = 20151125
below = row + col - 2
below = below * (below+1)
below //= 2

position = below + col - 1

print("Part 1:", (20151125 * pow_mod(252533, position, 33554393)) % 33554393)
