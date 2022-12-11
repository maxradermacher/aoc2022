import math
import sys


class Monkey:
    def __init__(self, items, operation, test, true_idx, false_idx):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_idx = true_idx
        self.false_idx = false_idx
        self.total = 0


monkeys = []
for group in sys.stdin.read().split("\n\n"):
    lines = group.split("\n")
    items = list(map(int, lines[1][18:].split(", ")))
    operator, amount = lines[2][23:].split(" ")
    test = int(lines[3][21:])
    true_idx = int(lines[4][29:])
    false_idx = int(lines[5][30:])

    def operation(old, operator=operator, amount=amount):
        if amount == "old":
            operand = old
        else:
            operand = int(amount)
        if operator == "+":
            return old + operand
        else:
            return old * operand

    monkeys.append(Monkey(items, operation, test, true_idx, false_idx))

for _ in range(20):
    for m in monkeys:
        items = m.items
        m.items = []
        m.total += len(items)
        for item in items:
            item = m.operation(item) // 3
            new_idx = m.true_idx if item % m.test == 0 else m.false_idx
            monkeys[new_idx].items.append(item)


print(math.prod(sorted([m.total for m in monkeys])[-2:]))
