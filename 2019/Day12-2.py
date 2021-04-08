import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

moons = [[1,3,-11], [17,-10,-8], [-1,-15,2], [12,-4,-4]]
vel = [[0,0,0] for i in range(4)]

xseen = set()
yseen = set()
zseen = set()
xs, ys, zs = 0,0,0

n = 0
while xs == 0 or ys == 0 or zs == 0:
  x = tuple([moons[i][0] for i in range(4)]+[vel[i][0] for i in range(4)])
  y = tuple([moons[i][1] for i in range(4)]+[vel[i][1] for i in range(4)])
  z = tuple([moons[i][2] for i in range(4)]+[vel[i][2] for i in range(4)])
  if n % 1000 == 0:  print(n, xs, ys, zs)
  if x in xseen and xs == 0:
    xs = n
#    xs = n
  if y in yseen and ys == 0:
    ys = n
#    ys = n
  if z in zseen and zs == 0:
    zs = n
#    zs = n

  xseen.add(x)
  yseen.add(y)
  zseen.add(z)

  # Update vels
  for i in range(len(moons)):
    for j in range(len(moons)):
      if i < j:
        if moons[i][0] < moons[j][0]:
          vel[i][0] += 1
          vel[j][0] -= 1
        elif moons[i][0] > moons[j][0]:
          vel[j][0] += 1
          vel[i][0] -= 1
        if moons[i][1] < moons[j][1]:
          vel[i][1] += 1
          vel[j][1] -= 1
        elif moons[i][1] > moons[j][1]:
          vel[j][1] += 1
          vel[i][1] -= 1
        if moons[i][2] < moons[j][2]:
          vel[i][2] += 1
          vel[j][2] -= 1
        elif moons[i][2] > moons[j][2]:
          vel[j][2] += 1
          vel[i][2] -= 1

  # Update moons:
  for i in range(len(moons)):
    moons[i] = [vel[i][0] + moons[i][0], vel[i][1] + moons[i][1], vel[i][2] + moons[i][2]]

  n += 1

print("fin")
print(xs,ys,zs)

print(lcm(lcm(xs, ys), zs))