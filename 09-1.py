import sys


DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pos = set((0, 0))
head, tail = (0, 0), (0, 0)
for l in sys.stdin:
    direction, distance = l.rstrip().split(" ")
    for _ in range(0, int(distance)):
        delta = DIRECTION["URDL".index(direction)]
        head = (head[0] + delta[0], head[1] + delta[1])
        print(tail)
        if abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2:
            tail = (head[0] - delta[0], head[1] - delta[1])
            pos.add(tail)
        print(tail)
