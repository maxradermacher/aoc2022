import sys

f = set()
b = set()

y = 2000000
for l in sys.stdin:
    sx, sy, bx, by = [int(v.strip("xy=,:\n")) for v in l.split(" ") if "=" in v]
    if by == y:
        b.add(bx)
    dist = abs(sx - bx) + abs(sy - by)
    width = dist - abs(sy - y)
    if width < 0:
        continue
    for n in range(sx - width, sx + width + 1):
        f.add(n)
print(len(f) - len(b))
