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

for (idx, xpos) in enumerate(v):
    pixel = idx % 40
    print("#" if abs(xpos - pixel) <= 1 else ".", end="")
    if pixel == 39:
        print()
