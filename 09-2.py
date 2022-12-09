import sys


DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def correction(head, tail):
    diff = (head[0] - tail[0], head[1] - tail[1])
    if abs(diff[0]) >= 2:
        return (diff[0] // abs(diff[0]), diff[1] // max(1, abs(diff[1])))
    if abs(diff[1]) >= 2:
        return (diff[0] // max(1, abs(diff[0])), diff[1] // abs(diff[1]))
    return (0, 0)


pos = set()
rope = [(0, 0)] * 10
pos.add((0, 0))
for l in sys.stdin:
    direction, distance = l.rstrip().split(" ")
    for _ in range(int(distance)):
        delta = DIRECTION["URDL".index(direction)]
        for idx in range(len(rope) - 1):
            rope[idx] = (rope[idx][0] + delta[0], rope[idx][1] + delta[1])
            delta = correction(rope[idx], rope[idx + 1])
        rope[-1] = (rope[-1][0] + delta[0], rope[-1][1] + delta[1])
        pos.add(rope[-1])
print(len(pos))
