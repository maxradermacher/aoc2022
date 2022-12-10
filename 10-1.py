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
for (idx, xval) in enumerate(v):
    if ((idx + 1) + 20) % 40 == 0:
        res += (idx + 1) * xval
print(res)
