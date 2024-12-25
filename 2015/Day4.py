from hashlib import md5

pzl_inp = input("Enter puzzle input:    ").strip()

i = 0
while True:
    hash = md5((pzl_inp + str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        print("Part 1:", i)
        break
    i += 1

i = 0
while True:
    hash = md5((pzl_inp + str(i)).encode()).hexdigest()
    if hash[:6] == "000000":
        print("Part 2:", i)
        break
    i += 1
