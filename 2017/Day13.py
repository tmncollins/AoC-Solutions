from _collections import *

with open("inputs/13.txt") as f:
    all_data = f.read().split("\n")


ranges = defaultdict(int)
end = 0


def get_catch(range):
    return (range - 1) * 2


def caught(time, depth, range):
    if range == 0: return False
    catch = get_catch(range)
    if (time) % catch == 0:
        return True
    return False


for line in all_data:
    line = line.strip()
    if line == "": continue

    a,b = list(map(int, line.split(":")))
    ranges[a] = b
    end = max(end, a)

# part 1
part1 = 0
for i in range(0, end+1):
    if caught(i, i, ranges[i]):
        part1 += i * ranges[i]
print("Part 1:", part1)

# part 2
catch = set()
for i in range(0, end+1):
    if ranges[i] != 0:
        catch.add((i, get_catch(ranges[i])))

delay = 0
while True:
    possible = True
    for c in catch:
        if (delay + c[0]) % c[1] == 0:
            possible = False
            break

    if possible:
        print("Part 2:", delay)
        break
    delay += 1

# we know any safe delays will repeat every n rounds, where n = lcm of all ranges.
# each scanner is essentially an arithmetic sequence. we want to find the smallest positive
# integer that is not in any of the sequences



