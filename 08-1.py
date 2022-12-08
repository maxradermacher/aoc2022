import sys

lines = sys.stdin.read().rstrip().split("\n")

vis = []
for l in lines:
    vis.append([False] * len(l))


iterations = [
    (range(0, len(lines), 1), range(0, len(lines[0]), 1)),
    (range(0, len(lines), 1), range(len(lines[0]) - 1, -1, -1)),
    (range(len(lines) - 1, -1, -1), range(0, len(lines[0]), 1)),
    (range(len(lines) - 1, -1, -1), range(len(lines[0]) - 1, -1, -1)),
]

rows = range(0, len(lines))
cols = range(0, len(lines[0]))

for row in rows:
    for order in [cols, reversed(cols)]:
        tallest = -1
        for col in order:
            height = int(lines[row][col])
            if height > tallest:
                tallest = height
                vis[row][col] = True

for col in cols:
    for order in [rows, reversed(rows)]:
        tallest = -1
        for row in order:
            height = int(lines[row][col])
            if height > tallest:
                tallest = height
                vis[row][col] = True

print(sum([1 if v else 0 for row in vis for v in row]))
