t = 373803594
with open('inputs/9.txt', 'r') as f: #open the file
    contents = list(map(int, f.readlines()))

def p2():
    start = 0
    end = 1
    while start < len(contents) and end < len(contents):
        s = sum(contents[start:end+1])
        if s == t:
            return min(contents[start:end+1]) + max(contents[start:end+1])
        elif s > t:
            start += 1
            end = start + 1
        else:
            end += 1

print(p2())
