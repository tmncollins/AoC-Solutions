from tkinter import *
import time

n = 1000
moons = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]


class alien(object):
    def __init__(self):
        self.root = Tk()
        self.size = 500
        self.canvas = Canvas(self.root, width=self.size, height=self.size, bg="black")
        self.canvas.pack()
        self.mult = 3
        self.radius = 3

        self.root.after(0, self.animation(500))
        self.root.mainloop()

    def animation(self, n):
        moons = [[5, -1, 5], [0, -14, 2], [16, 4, 0], [18, 1, 16]]
        vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        colours = ["red", "blue", "green", "yellow"]
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
            self.canvas.delete("all")
            moonsinorder = []  # sorted by z; z,x,y
            for moon in moons:
                moonsinorder.append((moon[2], moon[0], moon[1]))
            c = {moonsinorder[i]: colours[i] for i in range(4)}
            moonsinorder = sorted(moonsinorder)

            for i in range(len(moonsinorder)):
                z, x, y = moonsinorder[i]
                m = self.mult
                x = x * m
                y = y * m
                z = z * m
                x += self.size
                y += self.size // 2
                z += self.size // 3

                # Y is controlled by x, y and z
                y = (4*y) + (z * 0.25) + (x* 0.25)
                y = int(y) // 4.5
                # X is controlled by x and z
                x = x-z
                x *= 0.8

                # r is perspective
                r = self.radius
                if z > 0:
                    r *= 0.02 * z
                elif z < 0:
                    r /= abs(z)

                self.canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill=c[moonsinorder[i]])
            self.canvas.update()

            time.sleep(0.25)


alien()

