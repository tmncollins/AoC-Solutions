
with open("inputs/9.txt") as f:
    stream = f.read().strip()

cancel = False
garbage = False

garbage_size = 0
depth = 0
score = 0

for c in stream:

    if cancel:
        cancel = False
        continue

    if garbage:
        if c not in "!>":
            garbage_size += 1

    if c == "{":
        if not garbage:
            depth += 1
    elif c == "}":
        if not garbage:
            score += depth
            depth -= 1
    elif c == "!":
        cancel = True
    elif c == "<":
        garbage = True
    elif c == ">":
        garbage = False

print("Part 1:", score)
print("Part 2:", garbage_size)

