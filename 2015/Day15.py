with open("inputs/Day15.txt") as f:
    data = f.read().split("\n")

ingredients = []

for line in data:
    if len(line) < 5: continue

    line = line.split()
    capacity = int(line[2].replace(",", ""))
    durability = int(line[4].replace(",", ""))
    flavour = int(line[6].replace(",", ""))
    texture = int(line[8].replace(",", ""))
    calories = int(line[10].replace(",", ""))

    ingredients.append([capacity, durability, flavour, texture, calories])

best = 0
best_lite = 0
for a in range(100):
    for b in range(100-a):
        for c in range(100-a-b):
            d = 100 - a - b - c
            if d < 0: continue

            capacity = 0
            durability = 0
            flavour = 0
            texture = 0
            calories = 0
            quant = [a,b,c,d]

            for i in range(4):
                capacity += quant[i] * ingredients[i][0]
                durability += quant[i] * ingredients[i][1]
                flavour += quant[i] * ingredients[i][2]
                texture += quant[i] * ingredients[i][3]
                calories += quant[i] * ingredients[i][4]

            if capacity < 0 or durability < 0 or flavour < 0 or texture < 0:
                continue

            score = capacity * durability * flavour * texture
            if score > best:
                best = score
            if score > best_lite and calories == 500:
                best_lite = score

print("Part 1:", best)
print("Part 1:", best_lite)

# 62842880
# 1152715212

