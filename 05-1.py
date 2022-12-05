import sys

start, delta = [x.split("\n")[:-1] for x in sys.stdin.read().split("\n\n")]
stack = [[] for _ in range((len(start[0]) + 1) // 4)]

for row in reversed(start):
    for i, arr in enumerate(stack):
        ch = row[(i * 4) + 1 : (i * 4) + 2]
        if ch != " ":
            arr.append(ch)

for row in delta:
    row = row.split(" ")
    n, src, dst = int(row[1]), int(row[3]) - 1, int(row[5]) - 1
    stack[dst].extend(reversed(stack[src][-n:]))
    del stack[src][-n:]

print("".join([x[-1] for x in stack]))
