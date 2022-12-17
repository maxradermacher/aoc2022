import sys

ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 1), (1, 2), (2, 1), (1, 0), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]
PATTERN = sys.stdin.read().rstrip()

ridx = 0
pidx = 0
rows = []
top = 0


def is_valid(r, x, y):
    if y < 0 or x < 0:
        return False
    for (vx, vy) in r:
        if x + vx > 6:
            return False
        if rows[y + vy][x + vx]:
            return False
    return True


extra = None
pat = []
det = []
while ridx < 1_000_000_000_000:
    pidx = pidx % len(PATTERN)
    if ridx % len(ROCKS) == 0 and extra is None:
        pat.append(pidx)
        det.append((ridx, top))
        for length in range(len(pat) // 4, 0, -1):
            r1 = pat[-length:]
            r2 = pat[-2 * length : -length]
            r3 = pat[-3 * length : -2 * length]
            r4 = pat[-4 * length : -3 * length]
            if r1 == r2 and r2 == r3 and r3 == r4:
                old, new = det[-1 - length], det[-1]
                cycles = (1_000_000_000_000 - new[0]) // (new[0] - old[0])
                ridx += cycles * (new[0] - old[0])
                extra = cycles * (new[1] - old[1])
    x = 2
    y = top + 3
    for _ in range(len(rows), y + 4):
        rows.append([False] * 7)
    r = ROCKS[ridx % len(ROCKS)]
    ridx += 1
    while True:
        dx = 1 if PATTERN[pidx] == ">" else -1
        pidx += 1
        pidx = pidx % len(PATTERN)
        if is_valid(r, x + dx, y):
            x += dx
        dy = -1
        if is_valid(r, x, y + dy):
            y += dy
        else:
            for (vx, vy) in r:
                rows[y + vy][x + vx] = True
                top = max(top, y + vy + 1)
            break

print("Done", top, extra, top + extra)
