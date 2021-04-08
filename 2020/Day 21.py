with open('inputs/21.txt', 'r') as f: #open the file
    contents = f.readlines()

from _collections import defaultdict

ingredients = []
seenA = set()
allA = set()
seenI = set()
allergens = defaultdict(set)
allI = set()

for line in contents:
#    print(line)
    ingred, aller = line.replace("\n", "").replace(")", "").split("(contains ")
    ingred = set(ingred.split())
    aller = set(aller.split(", "))
    allA = allA.union(aller)
    allI = allI.union(ingred)
    ingredients.append([ingred, aller])

for item in allA:
    allergens[item] = set(allI)

ALLERGEN = defaultdict(str)

print(ingredients)
while len(allA) > len(seenA):
#    print(seenA)
#    print(allA, seenA)
    for a in range(len(ingredients)):
        # remove all known allergens
        A = ingredients[a]
        for item in seenI:
            if item in A[0]:
                A[0].remove(item)
        for item in seenA:
            if item in A[1]:
                A[1].remove(item)
        # check if only 1 ingredient
        if len(A[0]) == len(A[1]) == 1:
            seenA.add(list(A[1])[0])
            seenI.add(list(A[0])[0])
            ALLERGEN[list(A[1])[0]] = list(A[0])[0]
        for b in range(a):
            # find intersection of allergens
            B = ingredients[b]
            print(A[1].intersection(B[1]))
#            input()
            if len(A[1].intersection(B[1])) == 1:
#                print(A[0].intersection(B[0]))
                if len(A[0].intersection(B[0])) == 1:
                    seenA.add(list(A[1].intersection(B[1]))[0])
                    seenI.add(list(A[0].intersection(B[0]))[0])
                    ALLERGEN[list(A[1].intersection(B[1]))[0]] = list(A[0].intersection(B[0]))[0]
                else:
                    toRemove = set()
                    al = list(A[1].intersection(B[1]))[0]
                    for item in allergens[al]:
                        if item not in A[0].intersection(B[0]):
                            toRemove.add(item)
                    for item in toRemove:
                        allergens[al].remove(item)
                    if len(allergens[al]) == 1:
                        ALLERGEN[al] = list(allergens[al])[0]
                        seenA.add(al)
                        seenI.add(list(allergens[al])[0])

# make sure all allergens are removed
for a in range(len(ingredients)):
    # remove all known allergens
    A = ingredients[a]
    for item in seenI:
        if item in A[0]:
            A[0].remove(item)
    for item in seenA:
        if item in A[1]:
            A[1].remove(item)

tot = 0
for item in ingredients:
    tot += len(item[0])

print(tot)

answer = []
for item in sorted(allA):
    answer.append(ALLERGEN[item])
print(",".join(answer))
