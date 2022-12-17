import sys

v = {}
n = 0
for l in sys.stdin:
    c = l.split(" ")
    name, rate, tunnels = c[1], int(c[4][5:-1]), list(map(lambda v: v[:-1], c[9:]))
    v[name] = (n, rate, tunnels)
    n += 1

res = 0
stack = [(0, 30, "AA", 0)]
b = {}
while len(stack) > 0:
    total, time, name, opened = stack.pop(0)
    if time == 0:
        res = max(res, total)
        continue
    best = b.get((name, opened), -1)
    if total <= best:
        continue
    b[(name, opened)] = total
    bit, rate, tunnels = v[name]
    for tunnel in tunnels:
        stack.append((total, time - 1, tunnel, opened))
    if (opened & (1 << bit)) == 0 and rate > 0:
        stack.append((total + (time - 1) * rate, time - 1, name, opened | (1 << bit)))

print(res)
