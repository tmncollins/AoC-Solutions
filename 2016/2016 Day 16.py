puzzle_input = "11100010111110100"
start = puzzle_input

def expand(n):
    b = n[::-1]
    b = b.replace("1", "2").replace("0", "1").replace("2", "0")
    return n + "0" + b

def checksum(n):
    check = ""
    for i in range(0, len(n), 2):
        if n[i] == n[i+1]: check += "1"
        else: check += "0"
    return check

def get_check(size, start):
    while len(start) < size:
        start = expand(start)

    start = start[:size]

    print("Length:", len(start))
    check = checksum(start)
    while len(check) % 2 == 0:
        print("Length:", len(check))
        check = checksum(check)

    return check

print("Part 1:", get_check(272, puzzle_input))
print("Part 2:", get_check(35651584, puzzle_input))
