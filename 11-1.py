import math
import sys

class Monkey:
    def __init__(self, items, op, test, t, f):
        self.items = items
        self.op = op
        self.test = test
        self.t = t
        self.f = f
        self.total = 0

monkeys = []
for monkey in sys.stdin.read().split("\n\n"):
    lines = monkey.split("\n")
    items = list(map(int, lines[1][18:].split(", ")))
    operator, amount = lines[2][23:].split(" ")
    divis = int(lines[3][21:])
    t = int(lines[4][29:])
    f = int(lines[5][30:])

    def operation(old, operator=operator, amount=amount):
        if amount == "old":
            operand = old
        else:
            operand = int(amount)
        if operator == "+":
            return old + operand
        else:
            return old * operand

    monkeys.append(Monkey(items, operation, divis, t, f))

for _ in range(20):
    for m in monkeys:
        items = m.items
        m.items = []
        m.total += len(items)
        for item in items:
            item = m.op(item) // 3
            monkeys[m.t if item % m.test == 0 else m.f].items.append(item)


print(math.prod(sorted([m.total for m in monkeys])[-2:]))
