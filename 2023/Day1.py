with open("inputs/Day1.txt", "r") as file:
    data = file.read().split("\n")

left = 0
right = 0
digits = list("0123456789")
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

part1 = 0
for line in data:
    x = ""
    for i in line:
        if i in digits:
            x += i
            break
    line = line[::-1]
    for i in line:
        if i in digits:
            x += i
            break
    if x == "": x = "0"
    part1 += int(x)

print("Part 1:", part1)

part2 = 0
for line in data:
    left = float("inf")
    left_digit = ""
    for i in digits:
        if i in line:
            pos = line.index(i)
            if pos < left:
                left = pos
                left_digit = i
    for i in numbers:
        if i in line:
            pos = line.index(i)
            if pos < left:
                left = pos
                left_digit = str(numbers.index(i))

    right = float("inf")
    right_digit = ""
    line = line[::-1]
    for i in digits:
        if i in line:
            pos = line.index(i)
            if pos < right:
                right = pos
                right_digit = i
    for j in numbers:
        i = j[::-1]
        if i in line:
            pos = line.index(i)
            if pos < right:
                right = pos
                right_digit = str(numbers.index(j))

    part2 += int(left_digit + right_digit)

print("Part 2:", part2)
