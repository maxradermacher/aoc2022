import sys

score = 0
for line in sys.stdin:
    line = line.rstrip()
    them, _, us = line
    them, us = "ABC".index(them), "XYZ".index(us)
    score += us + 1
    if them == us:
        score += 3
    elif (them + 1) % 3 == us:
        score += 6

print(score)
