from functools import lru_cache

with open("inputs/Day9.txt") as f:
    data = f.read().strip()

@lru_cache(maxsize=None)
def decompress(data, part2=False):
#    print(data)
    if "(" not in data: return len(data)
    i = 0
    ans = 0
    last = 0

    while i < len(data):
        if data[i] == "(":
            ans += i-last
            for j in range(i, len(data)):
                if data[j] == ")": break
            look = data[i:j].replace("(", "").replace(")", "").split("x")
            length = int(look[0])
            times = int(look[1])

            if part2:
                ans += decompress(data[j+1:j+1+length], True) * times
            else:
                ans += times*length

            i = j+length+1
            last = i
        else:
            i += 1

    return ans + len(data) - last

print("Part 1:", decompress(data))
print("Part 2:", decompress(data, True))

