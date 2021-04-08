from functools import lru_cache

with open('inputs/7.txt', 'r') as f: #open the file
    contents = f.readlines()

fits = dict()

for line in contents:
    b, con = line.split("contain")
    b = b.strip()
    bags = con.split(",")
    bb = []
    for i in range(len(bags)):
        bag = bags[i]
        bag = bag.split()[1:]
        if bag[-1][-1] != "s": bag[-1] = "bags"
        bag = " ".join(bag).replace(".", "")
        if bags[i].split()[0] != "no":
            for i in range(int(bags[i].split()[0])):
                bb.append(bag)
    fits[b] = bb

bags = list(fits.keys())

count = 0

#print(fits)

@lru_cache(maxsize=None)
def countBags(bag):
#    print(bag)
    global fits
    ans = 1
    for item in fits[bag]:
        ans += countBags(item)
    return ans

print(countBags("shiny gold bags") - 1)
