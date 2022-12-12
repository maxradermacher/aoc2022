import sys

e = [list(map(ord, list(line))) for line in sys.stdin.read().rstrip().split("\n")]
w, h = len(e[0]), len(e)

for (row, vals) in enumerate(e):
    for (col, val) in enumerate(vals):
        if ord("E") == val:
            start = (row, col)
        if ord("S") == val:
            finish = (row, col)

e[start[0]][start[1]] = ord("z")
e[finish[0]][finish[1]] = ord("a")

stack = []
stack.append((0, start))

visited = [[False] * w for _ in range(h)]
while True:
    n, pos = stack.pop(0)
    if e[pos[0]][pos[1]] == ord("a"):
        print(n)
        break
    for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        npos = (pos[0] + delta[0], pos[1] + delta[1])
        if npos[0] < 0 or npos[0] >= h or npos[1] < 0 or npos[1] >= w:
            continue
        if visited[npos[0]][npos[1]]:
            continue
        if e[npos[0]][npos[1]] >= e[pos[0]][pos[1]] - 1:
            visited[npos[0]][npos[1]] = True
            stack.append((n + 1, npos))
