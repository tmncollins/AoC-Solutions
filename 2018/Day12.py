with open("input/12.txt") as f:
    all_data = f.read().split("\n")

stay_alive = set()



x = 0
plants = ""
left_pot = -2
for line in all_data:
    if x == 0:
        x = 1
        line = line.split()
        plants = ".." + line[2] + ".."
        continue

    if line == "": continue
    state, new = line.split(" => ")
    if "#" in new:
        stay_alive.add(state)


def count_pots(plants, left_pot):
    cnt = 0
    for i in range(len(plants)):
        if plants[i] == "#":
            cnt += i + left_pot
    return cnt


def trim(plants, left_pot):
    for i in range(len(plants)):
        if plants[i] == "#":
            if i >= 2:
                left_pot += i - 2
                plants = plants[i-2:]
                break

    for i in range(len(plants)-1, -1, -1):
        if plants[i] == "#":
            if i+3 <= len(plants)-1:
                plants = plants[:i+3]
                break

    return plants, left_pot


def predict(scores, delta, start, outcome):
    d = scores[start + delta] - scores[start]
    outcome -= start + 1
    return scores[start] + d * (outcome // delta)


def find_seq(scores):
    for i in range(1, len(scores) // 4):
        for start in range(len(scores) // 4):
            valid = True
            ptr = start + i
            d = scores[ptr] - scores[start]
            while ptr < len(scores):
                if scores[ptr] - scores[ptr-i] != d:
                    valid = False
                    break
                ptr += i

            if valid: return i, start


last_plants = plants
scores = []
for gen in range(1000):
    plants = "..." + plants + "..."
#    print(plants)
    new_plants = ""
    for i in range(2, len(plants) - 2):
        if plants[i-2:i+3] in stay_alive:
            new_plants += "#"
        else:
            new_plants += "."
#    plants, left_pot = trim(new_plants, left_pot)
    plants = new_plants
    left_pot -= 1

#    print(plants, left_pot, gen)

    if gen == 19:
        print("Part 1:", count_pots(plants, left_pot))

    scores.append(count_pots(plants, left_pot))

    if plants == last_plants: break
    last_plants = plants

delta, start = find_seq(scores)
print("Part 2:", predict(scores, delta, start, 50000000000))

