import sys

x = 1
v = []
for l in sys.stdin:
    cmd, _, arg = l.rstrip().partition(" ")
    if cmd == "noop":
        v.append(x)
    if cmd == "addx":
        v.append(x)
        v.append(x)
        x += int(arg)

res = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    if cycle <= len(v):
        res += cycle * v[cycle - 1]
print(res)
