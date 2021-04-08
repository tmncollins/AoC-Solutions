with open('inputs/1.txt', 'r') as f: #open the file
    contents = set(map(int, f.readlines()))

t = 2020

for a in contents:
    for b in contents:
        for c in contents:
            if a + b + c == t:
                print(a*b*c)