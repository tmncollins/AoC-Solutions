start =  248345
end =  746315
ans = 0
for i in range(start, end):
    double = False
    inc = True
    last = ""
    last2 = ""
    for item in list(str(i)):
        if last != "" and item == last: double = True
        if last != "" and int(last) > int(item): inc = False
        last = item
#    print(i, inc, double)
    if inc and double: ans += 1
print(ans)