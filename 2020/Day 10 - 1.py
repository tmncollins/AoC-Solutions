with open('inputs/10.txt', 'r') as f: #open the file
    contents = list(map(int, f.readlines()))

onedif = 0
threedif = 0
contents = sorted(contents)
contents.insert(0,0)
contents.append(contents[-1] + 3)
for i in range(1,len(contents)):
    if contents[i] - contents[i-1] == 1: onedif += 1
    elif contents[i] - contents[i-1] == 3: threedif += 1

print(onedif, threedif)
print(threedif * onedif)