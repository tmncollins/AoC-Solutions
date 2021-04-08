start =  248345
end =  746315
#start = 111444
#end = start + 1
ans = 0
for i in range(start, end):
    double = False
    inc = True
    last = ""
    last2 = ""
    for j in range(len(list(str(i)))):
        item = str(i)[j]
        if j == 1:
            next = str(i)[j+1]
            if last != "" and item == last and item != next: double = True
        if j < len(str(i)) - 1:
            next = str(i)[j+1]
            if last != "" and last2 != "" and item == last and last != last2 and item != next: double = True
        else:
            if last != "" and last2 != "" and item == last and last != last2: double = True
        if last != "" and int(last) > int(item): inc = False
        last2 = last
        last = item
#    print(i, inc, double)
    if inc and double: ans += 1
print(ans)