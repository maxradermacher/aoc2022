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


for _ in range(2022):
    x = 2
    y = top + 3
    for _ in range(len(rows), y + 4):
        rows.append([False] * 7)
    r = ROCKS[ridx % len(ROCKS)]
    ridx += 1
    while True:
        dx = 1 if PATTERN[pidx % len(PATTERN)] == ">" else -1
        pidx += 1
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

print(top)
