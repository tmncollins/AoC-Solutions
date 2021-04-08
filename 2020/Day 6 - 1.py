with open('inputs/6.txt', 'r') as f: #open the file
    contents = f.readlines()

alpha = list("abcdefghijklmnopqrstuvwxyz")
last = ""
tot = 0
for line in contents:
    line = line.replace("\n", "")
    if line.replace(" ", "") == "":
        count = 0
        for a in alpha:
            if last.count(a) > 0:
                count += 1
        tot += count
        last = ""
    else:
        last += line

print(tot)