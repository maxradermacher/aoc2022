import sys

t = [list(map(int, list(line))) for line in sys.stdin.read().rstrip().split("\n")]
w, h = len(t[0]), len(t)
visible = [[False] * w for _ in range(0, h)]
sight_paths = [
    *[[(row, col) for col in range(0, w)] for row in range(0, h)],
    *[[(row, col) for row in range(0, h)] for col in range(0, w)],
]
for sight_path in sight_paths + list(map(reversed, sight_paths)):
    tallest = -1
    for (row, col) in sight_path:
        if t[row][col] > tallest:
            tallest = t[row][col]
            visible[row][col] = True
print(sum([1 if v else 0 for r in visible for v in r]))
