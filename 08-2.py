import math
import sys

heights = [list(map(int, list(line))) for line in sys.stdin.read().rstrip().split("\n")]

w, h = len(heights[0]), len(heights)


def enumerate_rows(col, start, end):
    return [(row, col) for row in range(start, end + 1)]


def enumerate_cols(row, start, end):
    return [(row, col) for col in range(start, end + 1)]


def viewing_distance(stop, sight_path):
    res = 0
    for (row, col) in sight_path:
        if heights[row][col] <= stop:
            res += 1
        if heights[row][col] >= stop:
            break
    return res


def main():
    res = 0
    for row in range(0, h):
        for col in range(0, w):
            sight_paths = [
                enumerate_rows(col, row + 1, h - 1),
                reversed(enumerate_rows(col, 0, row - 1)),
                enumerate_cols(row, col + 1, w - 1),
                reversed(enumerate_cols(row, 0, col - 1)),
            ]
            viewing_distances = []
            for sight_path in sight_paths:
                viewing_distances.append(
                    viewing_distance(heights[row][col], sight_path)
                )
            scenic_score = math.prod(viewing_distances)
            if scenic_score > res:
                res = scenic_score
    return res


print(main())
