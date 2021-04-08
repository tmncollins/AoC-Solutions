with open('inputs/1.txt', 'r') as f: #open the file
    contents = set(map(int, f.readlines()))

t = 2020

for item in contents:
    if t - item in contents:
        print((t-item) * item)




