import sys

f = set()
m = 0
for l in sys.stdin:
    pts = [tuple(map(int, pt.split(","))) for pt in l.rstrip().split(" -> ")]
    for (s, e) in zip(pts, pts[1:]):
        if s[0] == e[0]:
            f.update([(s[0], n) for n in range(min(s[1], e[1]), max(s[1], e[1]) + 1)])
        if s[1] == e[1]:
            f.update([(n, s[1]) for n in range(min(s[0], e[0]), max(s[0], e[0]) + 1)])
        m = max(m, s[1], e[1])


def drop_sand(pos):
    if pos[1] == m + 1:
        return None
    for delta in [(0, 1), (-1, 1), (1, 1)]:
        new = (pos[0] + delta[0], pos[1] + delta[1])
        if new in f:
            continue
        return new
    return None


def place_sand():
    pos = (500, 0)
    while True:
        new = drop_sand(pos)
        if new is None:
            f.add(pos)
            return
        pos = new


n = 0
while (500, 0) not in f:
    place_sand()
    n += 1
print(n)
