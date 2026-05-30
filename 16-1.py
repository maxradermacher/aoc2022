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
    res = max(res, total)
    if time == 1:
        break
    best = b.get((name,), -1)
    if total <= best:
        continue
    b[(name,)] = total
    bit, rate, tunnels = v[name]
    if (opened & (1 << bit)) == 0 and rate > 0:
        stack.append((total + (time - 1) * rate, time - 1, name, opened | (1 << bit)))
    for tunnel in tunnels:
        stack.append((total, time - 1, tunnel, opened))

print(res)
