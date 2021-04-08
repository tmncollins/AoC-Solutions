with open('inputs/7.txt', 'r') as f: #open the file
    contents = f.readlines()

fits = dict()

for line in contents:
    b, con = line.split("contain")
    b = b.strip()
    bags = con.split(",")
    for i in range(len(bags)):
        bag = bags[i]
        bag = bag.split()[1:]
        if bag[-1][-1] != "s": bag[-1] = "bags"
        bag = " ".join(bag).replace(".", "")
        bags[i] = bag
    if bags == ["other bags"]:
        bags = []
    fits[b] = bags

bags = list(fits.keys())

print(bags)

count = 0
for bag in bags:
    pending = [bag]
    seen = set([bag])
    found = False
    while pending:
        look = pending.pop(0)
        for item in set(fits[look]):
            if item not in seen:
                if item == "shiny gold bags":
                    count += 1
                    found = True
                    break
                pending.append(item)
        if found: break
print(count)
