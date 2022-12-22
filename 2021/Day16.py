data = open("inputs/Day16.txt").read().replace("\n", "")

code = ""
version_sum = 0

h_to_b = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100",
        "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001",
        "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}


def to_bin(data):
    code = ""
    for a in data:
        code += h_to_b[a]
    return code


ptr = 0
bin_string = to_bin(data)


class Packet:

    def __init__(self):
        self.version = -1
        self.type = -1
        self.data = []
        self.length_type = -1

    def to_math_str(self):
        string = "("
        if self.type == 0:
            for d in self.data:
                string += d.to_math_str() + "+"
            string = string[:-1]
        elif self.type == 1:
            for d in self.data:
                string += d.to_math_str() + "*"
            string = string[:-1]
        elif self.type == 4:
            return str(self.data[0])
        elif self.type == 2:
            string = ""
            string += "min(["
            for d in self.data:
                string += d.to_math_str() + ","
            string = string[:-1] + "]"
        elif self.type == 3:
            string = ""
            string += "max(["
            for d in self.data:
                string += d.to_math_str() + ","
            string = string[:-1] + "]"
        elif self.type == 5:
            string += self.data[0].to_math_str() + ">" + self.data[1].to_math_str()
        elif self.type == 6:
            string += self.data[0].to_math_str() + "<" + self.data[1].to_math_str()
        elif self.type == 7:
            string += self.data[0].to_math_str() + "==" + self.data[1].to_math_str()

        return string + ")"

    def __str__(self):
        string = "<Packet: Version: " + str(self.version) + " ; Type: " + str(self.type) + " ; Data: ["
        for d in self.data:
            string += str(d) + ", "
        string = string[:-2]
        string += "]>"
        return string

    def __int__(self):
        if self.type == 0:
            tot = 0
            for d in self.data:
                tot += int(d)
            return tot
        elif self.type == 1:
            tot = 1
            for d in self.data:
                tot *= int(d)
            return tot
        elif self.type == 2:
            ans = float("inf")
            for d in self.data:
                ans = min(ans, int(d))
            return ans
        elif self.type == 3:
            ans = 0
            for d in self.data:
                ans = max(ans, int(d))
            return ans
        elif self.type == 4:
            return self.data[0]
        elif self.type == 5:
            return 1 if int(self.data[0]) > int(self.data[1]) else 0
        elif self.type == 6:
            return 1 if int(self.data[0]) < int(self.data[1]) else 0
        elif self.type == 7:
            return 1 if int(self.data[0]) == int(self.data[1]) else 0


def parse_packets_1(NUM, output=""):
    global ptr, version_sum

    packets = []
    while len(packets) < NUM:

        p = Packet()

        p.version = int(bin_string[ptr:ptr + 3], 2)
        version_sum += p.version
        ptr += 3
        p.type = int(bin_string[ptr:ptr + 3], 2)
        ptr += 3

        # literal
        if p.type == 4:
            number = ""
            while True:
                number += bin_string[ptr + 1:ptr + 5]
                ptr += 5
                if bin_string[ptr - 5] == "0":
                    break
            p.data = [int(number, 2)]

            packets.append(p)
            continue

        # operator
        p.length_type = int(bin_string[ptr])
        ptr += 1

        if p.length_type == 0:
            num = int(bin_string[ptr:ptr + 15], 2)
            ptr += 15
            p.data = parse_packets(num, output + "-")

        elif p.length_type == 1:
            num = int(bin_string[ptr:ptr + 11], 2)
            ptr += 11
            p.data = parse_packets_1(num, output + "-")

        packets.append(p)

    return packets


def parse_packets(num, output=""):
    global ptr, version_sum

#    while num % 4 != 0: num += 1

    end = ptr + num
    packets = []

    while ptr < end:

        if "1" not in bin_string[ptr:]: break

        p = Packet()

#        print(bin_string[ptr:])

        p.version = int(bin_string[ptr:ptr+3], 2)
        version_sum += p.version
        ptr += 3
        p.type = int(bin_string[ptr:ptr+3], 2)
        ptr += 3

        # literal
        if p.type == 4:
            number = ""
            while True:
                number += bin_string[ptr + 1:ptr + 5]
                ptr += 5
                if bin_string[ptr-5] == "0":
                    break
            p.data = [int(number, 2)]

            packets.append(p)
            continue

        # operator
        p.length_type = int(bin_string[ptr])
        ptr += 1

#        print(bin_string[ptr:])

        if p.length_type == 0:
            num = int(bin_string[ptr:ptr+15], 2)
            ptr += 15
            p.data = parse_packets(num, output + "-")

        elif p.length_type == 1:
            num = int(bin_string[ptr:ptr+11], 2)
            ptr += 11
            p.data = parse_packets_1(num, output + "-")

        packets.append(p)

    return packets

#print(bin_string)
p = parse_packets(len(bin_string), output="+")
p = p[0]

print("Part 1:", version_sum)
print("Part 2:", int(p))



"""
((24722196487)+((min((((max((((max((((max(((min(((max(((((289540*47376*(max(2100,435656,430083,15789783))*((971>971)*10691)))))))*13*(min(934,178,6235,758664,7238))*(11512421+896)*(min(2)))))))))))))),(9564307436))))+((14*8*13)+(5*2*3)+(3*2*7))+(58771*(1279<3399))))))+1336+(max(68277310806,2850))+(61*119))

"""


