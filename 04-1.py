import sys

score = 0
for line in sys.stdin:
    rs = [x.split("-") for x in line.rstrip().split(",")]
    rs = sorted([(int(x[0]), int(x[1])) for x in rs])
    if rs[1][0] >= rs[0][0] and rs[1][1] <= rs[0][1]:
        score += 1
    elif rs[0][0] >= rs[1][0] and rs[0][1] <= rs[1][1]:
        score += 1
print(score)
