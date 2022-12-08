import math
import sys

t = [list(map(int, list(line))) for line in sys.stdin.read().rstrip().split("\n")]
w, h = len(t[0]), len(t)


def enumerate_rows(col, start, end):
    return [(row, col) for row in range(start, end)]


def enumerate_cols(row, start, end):
    return [(row, col) for col in range(start, end)]


def view_dist(stop, sight_path):
    res = 0
    for (row, col) in sight_path:
        if t[row][col] <= stop:
            res += 1
        if t[row][col] >= stop:
            break
    return res


def main():
    res = 0
    for (row, col) in [(r, c) for r in range(0, h) for c in range(0, w)]:
        sight_paths = [
            enumerate_rows(col, row + 1, h),
            reversed(enumerate_rows(col, 0, row)),
            enumerate_cols(row, col + 1, w),
            reversed(enumerate_cols(row, 0, col)),
        ]
        res = max(res, math.prod([view_dist(t[row][col], x) for x in sight_paths]))
    return res


print(main())
