from intcode import Intcode

data = [109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1105,1,259,1201,1,0,221,203,1,21101,31,0,0,1105,1,282,21102,38,1,0,1105,1,259,21001,23,0,2,21201,1,0,3,21101,1,0,1,21102,57,1,0,1106,0,303,2102,1,1,222,21001,221,0,3,20102,1,221,2,21101,259,0,1,21102,80,1,0,1106,0,225,21101,0,167,2,21101,0,91,0,1105,1,303,2102,1,1,223,20102,1,222,4,21102,1,259,3,21102,1,225,2,21102,225,1,1,21102,1,118,0,1106,0,225,21001,222,0,3,21102,1,93,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,2101,0,1,223,21001,221,0,4,20102,1,222,3,21102,21,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,106,0,108,20207,1,223,2,21001,23,0,1,21101,-1,0,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,21202,-3,1,1,21202,-2,1,2,21201,-1,0,3,21101,0,250,0,1105,1,225,22101,0,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0]
computer = Intcode(data)

n = 50
grid = [[0 for i in range(n)] for j in range(n)]

tot = 0
for y in range(n):
    for x in range(n):
        computer = Intcode(data)
        computer.nextI(x)
        computer.nextI(y)
        out = computer.nextO()
        grid[y][x] = out[0]
        if out[0] == 1: tot += 1
print(tot)

for y in range(n):
    for x in range(n):
        print(grid[y][x], end="")
    print()