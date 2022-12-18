with open("inputs/Day11.txt") as f:
    all_data = f.read().split("\n")

def add(a, b):
    return a + b

def times(a, b):
    return a * b

def double(a, b):
    return a * 2

def square(a, b):
    return a ** 2

monkeys = dict()
MAX_NUM = 1


class Monkey:
    global monkeys, MAX_NUM

    def __init__(self, id, items, operation, operation_val, div, true, false, part2 = False):
        self.id = id
        self.items = items
        self.operation = operation
        self.op_val = operation_val
        self.div = div
        self.true = true
        self.false = false
        self.count = 0
        self.part2 = part2

    def inspect_item(self, item):
        self.count += 1
        item = self.operation(item, self.op_val)
        if self.part2:
            item %= MAX_NUM
        else:
            item = int(item / 3)

        if item % self.div == 0:
            monkeys[self.true].items.append(item)
        else:
            monkeys[self.false].items.append(item)

    def inspect_items(self):
        items = self.items
        self.items = []

        for item in items:
            self.inspect_item(item)

    def __str__(self):
        string = "<Monkey " + str(self.id) + ": ["
        for item in self.items:
            string += str(item) + ", "
        if len(self.items) > 0:
            string = string[:-2]
        string += "]; if divisible by " + str(self.div) + " then give to " + str(self.true) + " else give to " + str(self.false) + ">"

        return string


all_data.append("")

def run(all_data, num_rounds, part2 = False):

    global MAX_NUM

    monkey_id = -1
    monkey_items = []
    monkey_operation = [add, 0]
    monkey_div = 0
    monkey_true = 0
    monkey_false = 0
    max_monkey = 0

    for line in all_data:
        if len(line) < 5:
            m = Monkey(monkey_id, monkey_items, monkey_operation[0], monkey_operation[1], monkey_div, monkey_true, monkey_false, part2)
            max_monkey = max(max_monkey, monkey_id)
            MAX_NUM *= monkey_div
            monkeys[monkey_id] = m
            monkey_id = -1
            monkey_items = []
            monkey_operation = [add, 0]
            monkey_div = 0
            monkey_true = 0
            monkey_false = 0
            continue

        line = line.strip()
        line = line.split()

        if line[0] == "Monkey":
            monkey_id = int(line[1].replace(":", ""))

        elif line[0] == "Starting":
            for i in range(2, len(line)):
                item = line[i].replace(",", "")
                monkey_items.append(int(item))

        elif line[0] == "Operation:":
            if line[4] == "*":
                if line[5] == "old":
                    monkey_operation[0] = square
                else:
                    monkey_operation[0] = times
                    monkey_operation[1] = int(line[5])
            elif line[4] == "+":
                if line[5] == "old":
                    monkey_operation[0] = double
                else:
                    monkey_operation[0] = add
                    monkey_operation[1] = int(line[5])
            else:
                print("Unknown operation")

        elif line[0] == "Test:":
            monkey_div = int(line[3])

        elif line[1] == "true:":
            monkey_true = int(line[5])

        elif line[1] == "false:":
            monkey_false = int(line[5])

    for round in range(num_rounds):
        for m in range(max_monkey + 1):
            monkey = monkeys[m]
            monkey.inspect_items()

    counts = []
    for monkey in monkeys.values():
        counts.append(monkey.count)

    counts = sorted(counts)

    return counts[-1] * counts[-2]

print("Part 1:", run(all_data, 20))
print("Part 2:", run(all_data, 10000, True))
