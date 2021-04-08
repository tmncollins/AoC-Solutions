with open('inputs/4.txt', 'r') as f: #open the file
    contents = f.readlines()

passports = 0

req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
curr = ""
for line in contents:
    if len(line) > 2:
        curr += line
    else:
        valid = True
        for item in req:
            if curr.count(item + ":") == 0:
                valid = False
                break
        if valid:
            passports += 1

        curr = ""
print(passports)