n = 1000

moons = [[1,3,-11], [17,-10,-8], [-1,-15,2], [12,-4,-4]]
vel   = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
for _ in range(n):
    for i in range(len(moons)):
        for j in range(len(moons)):
            if i != j and i < j:
                if moons[i][0] > moons[j][0]:
                    vel[i][0] -= 1
                    vel[j][0] += 1
                elif moons[i][0] < moons[j][0]:
                    vel[i][0] += 1
                    vel[j][0] -= 1

                if moons[i][1] > moons[j][1]:
                    vel[i][1] -= 1
                    vel[j][1] += 1
                elif moons[i][1] < moons[j][1]:
                    vel[i][1] += 1
                    vel[j][1] -= 1

                if moons[i][2] > moons[j][2]:
                    vel[i][2] -= 1
                    vel[j][2] += 1
                elif moons[i][2] < moons[j][2]:
                    vel[i][2] += 1
                    vel[j][2] -= 1
    for i in range(len(moons)):
        moons[i] = [moons[i][0] + vel[i][0], moons[i][1] + vel[i][1], moons[i][2] + vel[i][2]]
        print(moons[i], vel[i])

    # Energy
    tot = 0
    for i in range(len(moons)):
        pot = 0
        kin = 0
        for item in moons[i]: pot += abs(item)
        for item in vel[i]: kin += abs(item)

        tot += pot * kin
#        print(pot, kin)

    print(tot)
    print()