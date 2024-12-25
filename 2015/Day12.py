with open("inputs/Day12.txt") as f:
    json = f.read().strip()

json = "" + json + "!!!!"

numbers = set("-1234567890")
num = ""
tot = 0

for i in range(len(json)-3):
    c = json[i]

    if c in numbers:
        num += c
    elif num != "":
        tot += int(num)
        num = ""

print("Part 1:", tot)

with open("inputs/Day12.txt") as f:
    json = f.read().strip()


def process(j):
    global tot

    if type(j) == list:
        for item in j:
            if type(item) == int:
                tot += item
            if type(item) == list or type(item) == dict:
                process(item)

    elif type(j) == dict:
        if "red" in j.values():
            return
        for item in j.values():
            if type(item) == int:
                tot += item
            if type(item) == list or type(item) == dict:
                process(item)


json = eval(json)
tot = 0
process(json)
print("Part 2:", tot)