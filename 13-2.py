import functools
import sys


def parse(line):
    stack = [[]]
    while True:
        if len(line) == 0:
            return stack.pop().pop()
        if line[0] == "[":
            stack.append([])
            line = line[1:]
            continue
        if line[0] == "]":
            done = stack.pop()
            stack[-1].append(done)
            line = line[1:]
            continue
        if line[0] == ",":
            line = line[1:]
            continue
        for (idx, ch) in enumerate(line):
            if ch.isdigit():
                continue
            stack[-1].append(int(line[:idx]))
            line = line[idx:]
            break


def compare(l1, l2):
    for (v1, v2) in zip(l1, l2):
        if isinstance(v1, list):
            res = compare(v1, [v2] if isinstance(v2, int) else v2)
        elif isinstance(v2, list):
            res = compare([v1] if isinstance(v1, int) else v1, v2)
        else:
            res = v1 - v2
        if res != 0:
            return res
    return len(l1) - len(l2)


packets = []
for l in [v for g in sys.stdin.read().rstrip().split("\n\n") for v in g.split("\n")]:
    packets.append(parse(l))

packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(compare))

total = 1
for (idx, packet) in enumerate(packets):
    if packet in ([[2]], [[6]]):
        total *= idx + 1
print(total)
