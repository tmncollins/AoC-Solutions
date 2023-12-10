from functools import lru_cache

@lru_cache(maxsize=None)
def isTrap(a,b,c):
    if a and b and not c: return True
    if not a and b and c: return True
    if a and not b and not c: return True
    if not a and not b and c: return True
    return False

with open("inputs/Day18.txt") as f:
    look = f.read().strip()


def get_safe(rows, look):
    safe = look.count(".")

    for i in range(rows):
        if (i+1) % 10000 == 0: print(i+1, "out of", rows+1)
        next = ""
        look = "." + look + "."
        for i in range(1,len(look)-1):
            a = look[i-1] == "^"
            b = look[i] == "^"
            c = look[i+1] == "^"
            if isTrap(a,b,c):
                next += "^"
            else:
                next += "."
        safe += next.count(".")

        look = next

    return safe

print("Part 1:", get_safe(39, look))
print("Part 2:", get_safe(400000-1, look))