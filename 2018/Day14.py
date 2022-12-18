pzl_inp = 939601
#pzl_inp = 59414

target = str(pzl_inp)

recipes = "37"
elf_1 = 0
elf_2 = 1

part1 = False
while target not in recipes[-len(target)-2:] or len(recipes) < pzl_inp + 10:
    sum = str(int(recipes[elf_1]) + int(recipes[elf_2]))
    recipes += sum
    elf_1 += 1 + int(recipes[elf_1])
    elf_2 += 1 + int(recipes[elf_2])
    elf_1 %= len(recipes)
    elf_2 %= len(recipes)
    if not part1 and len(recipes) > pzl_inp + 10:
        part1 = True
        print("Part 1: ", end="")
        for i in range(10):
            print(recipes[pzl_inp + i], end="")
        print()

#    if len(recipes) % 100000 == 0: print(len(recipes))

if not part1:
    print("Part 1: ", end="")
    for i in range(10):
        print(recipes[pzl_inp + i], end="")
    print()

recipes_str = "".join(list(map(str, recipes)))
print("Part 2:", recipes_str.index(str(pzl_inp)))


