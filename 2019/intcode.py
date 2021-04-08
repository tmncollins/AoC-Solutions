from collections import defaultdict

class Intcode():
    def __init__(self, data=[]):
        self.data = defaultdict(int)
        self.index = 0
        self.base = 0
        self.orig = data.copy()
        self.print = False
        self.debug = False
        self.data = defaultdict(int)
        for i in range(len(data)):
            self.data[i] = data[i]

    def reset(self):
        self.index = 0
        self.base = 0
        self.data = defaultdict(int)
        for i in range(len(self.orig)):
            self.data[i] = self.orig[i]

    def store(self, mode, p, value):
        if mode == "0":
            a = self.data[self.index + p]
            self.data[a] = value
        elif mode == "2":
            a = self.data[self.index + p]
            self.data[a + self.base] = value

    def setPrintOutput(self, b=bool):
        self.print = b

    def getNum(self, mode, p):
        if mode == "0":
            p = self.data[self.index + p]
            return self.data[p]
        elif mode == "1":
            p = self.data[self.index + p]
            return p
        elif mode == "2":
            p = self.data[self.index + p]
            return self.data[p + self.base]

    def opCode01(self, mode1, mode2, mode3):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)
        self.store(mode3, 3, a + b)
        self.index += 4

    def opCode02(self, mode1, mode2, mode3):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)
        self.store(mode3, 3, a * b)
        self.index += 4

    def opCode03(self, inp, mode1):
        self.store(mode1, 1, inp)
        self.index += 2

    def opCode04(self, mode1):
        a = self.getNum(mode1, 1)
        if self.print:
            print(a)
        self.index += 2
        return a

    def opCode05(self, mode1, mode2):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)

        if a != 0:
            self.index = b
        else:
            self.index += 3

    def opCode06(self, mode1, mode2):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)

        if a == 0:
            self.index = b
        else:
            self.index += 3

    def opCode07(self, mode1, mode2, mode3):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)

        if a < b:
            self.store(mode3, 3, 1)
        else:
            self.store(mode3, 3, 0)

        self.index += 4

    def opCode08(self, mode1, mode2, mode3):
        a = self.getNum(mode1, 1)
        b = self.getNum(mode2, 2)

        if a == b:
            self.store(mode3, 3, 1)
        else:
            self.store(mode3, 3, 0)

        self.index += 4

    def opCode09(self, mode1):
        a = self.getNum(mode1, 1)
        self.base += a
        self.index += 2

    def get(self, index=0):
        return self.data[index]

    def nextI(self, inp):  # Run until next Input
        inputted = False
        o = []
        while not inputted and not self.isTerminated():
            result = self.next(inp)
            inputted = result[0]
            output = result[1]
            if output != "":
                o.append(output)
        return o

    def nextO(self, inp=[0]):  # Run until next Output
        outputted = False
        inpC = 0
        while not outputted:
            result = self.next(inp[inpC])
            inputted = result[0]
            if inputted:
                inpC += 1
                inpC = inpC % len(inp)  # Prevents crashes
            output = result[1]
            if output != "":
                outputted = True
                return (output, inpC)

    def nextIO(self, inp=0):  # Run until next Input or Output
        outputted = False
        inputted = False
        while not outputted and not inputted:
            result = self.next(inp)
            inputted = result[0]
            if inputted:
                return "inp"  # 1 represents requires input
            output = result[1]
            outputted = output != ""
            if outputted:
                return str(output)

    def setDebug(self, b=bool):
        self.debug = b

    def next(self, inp=0):
        code = "00000" + str(self.data[self.index])
        opCode = code[-2:]
        mode1 = code[-3]
        mode2 = code[-4]
        mode3 = code[-5]

        if self.debug:
            if code != "0000099":
                print(code)

        out = ""  # OUTPUT
        inpUsed = False

        #        print(code)

        if opCode == "01":
            self.opCode01(mode1, mode2, mode3)
        elif opCode == "02":
            self.opCode02(mode1, mode2, mode3)
        elif opCode == "03":
            self.opCode03(inp, mode1)
            inpUsed = True
        elif opCode == "04":
            out = self.opCode04(mode1)
        elif opCode == "05":
            self.opCode05(mode1, mode2)
        elif opCode == "06":
            self.opCode06(mode1, mode2)
        elif opCode == "07":
            self.opCode07(mode1, mode2, mode3)
        elif opCode == "08":
            self.opCode08(mode1, mode2, mode3)
        elif opCode == "09":
            self.opCode09(mode1)

        return (inpUsed, out)

    def isTerminated(self):
        return self.data[self.index] == 99