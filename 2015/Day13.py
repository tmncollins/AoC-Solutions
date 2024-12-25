from itertools import permutations

with open("inputs/Day13.txt") as f:
    data = f.read().split("\n")

happiness = dict()
people = set()

for line in data:
    if len(line) < 5: continue

    line = line.split()
    person = line[0]
    happy = int(line[3])
    if line[2] == "lose": happy *= -1
    neighbour = line[-1].replace(".", "")

    people.add(person)
    happiness[(person, neighbour)] = happy


def best_arrangement(people):
    global happiness

    highest = 0
    for arrangement in permutations(people):
        score = 0
        arrangement = list(arrangement)
        x = len(arrangement)

        for i in range(x):
            person = arrangement[i]
            left = arrangement[(i-1+x)%x]
            right = arrangement[(i+1)%x]
            score += happiness[(person, left)] + happiness[(person, right)]

        highest = max(highest, score)

    return highest


print("Part 1:", best_arrangement(people))

for person in people:
    happiness[(person, "Me")] = happiness[("Me", person)] = 0
people.add("Me")

print("Part 2:", best_arrangement(people))

