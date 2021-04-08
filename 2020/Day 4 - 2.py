with open('inputs/4.txt', 'r') as f: #open the file
    contents = f.readlines()

passports = 0

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
curr = ""
for line in contents:
    if len(line) > 2:
        curr += " " + line
    else:
        curr = curr.split()

        valid = True
        seen = list(req)
#        print(seen)
        for item in curr:
            t,i= item.split(":")
            if t in seen: seen.remove(t)
            elif t != "cid": valid = False
            if t == "byr":
                i = int(i)
                if i > 2002 or i < 1920: valid = False
            elif t == "iyr":
                i = int(i)
                if i > 2020 or i < 2010: valid = False
            elif t == "eyr":
                i = int(i)
                if i > 2030 or i < 2020: valid = False
            elif t == "hgt":
                type = i[-2:]
                i = i[:-2]
                if type == "in":
                    i = int(i)
                    if i > 76 or i < 59: valid = False
                elif type == "cm":
                    i = int(i)
                    if i > 193 or i < 150: valid = False
                else:
                    valid = False
            elif t == "hcl":
                if i[0] != "#" or len(i) != 7:
                    valid = False
                else:
                    for j in range(1,7):
                        if i[j] not in list("0123456789abcdef"):
                            valid = False
                            break
            elif t == "ecl":
                if i not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: valid = False
            elif t == "pid":
                try:
                    q = int(i)
                    if len(i) != 9: valid = False
                except:
                    valid = False
#            print(t,i,valid)
            if not valid: break

        if valid and len(seen) == 0:
            print(sorted(curr), passports)
            passports += 1

        curr = ""
print(passports)