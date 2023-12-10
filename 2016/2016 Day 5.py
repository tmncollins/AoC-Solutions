from hashlib import md5

pzl_inp = input("Enter puzzle input:    ").strip()

i = 0
code = ""
code2 = ["_" for _ in range(8)]
cnt = 0

while True:
    hash = md5((pzl_inp + str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        if len(code) < 8:
            code += hash[5]
            print(code)
            if len(code) == 8:
                print("Part 1:", code)

        try:
            pos = int(hash[5])
            if code2[pos] == "_":
                code2[pos] = hash[6]
                print("".join(code2))
                cnt += 1
                if cnt == 8:
                    print("Part 2:", "".join(code2))
                    break
        except:
            pass

    i += 1