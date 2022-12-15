import sys

inp = []
for l in sys.stdin:
    sx, sy, bx, by = [int(v.strip("xy=,:\n")) for v in l.split(" ") if "=" in v]
    inp.append((sx, sy, bx, by, abs(sx - bx) + abs(sy - by)))
inp.sort()

for y in range(4_000_000):
    r1 = None
    for (sx, sy, bx, by, dist) in inp:
        width = dist - abs(sy - y)
        if width < 0:
            continue
        r2 = (sx - width, sx + width + 1)
        if r1 is None:
            r1 = r2
        elif r2[0] <= r1[1] and r1[0] <= r2[1]:
            r1 = (min(r1[0], r2[0]), max(r1[1], r2[1]))
    if r1[1] < 4_000_000:
        print(r1[1] * 4_000_000 + y)
