import sys

score = 0
for line in sys.stdin:
    them, _, us = line.rstrip()
    them, us = "ABC".index(them), "XYZ".index(us)
    score += us + 1
    score += (us - them + 1) % 3 * 3

print(score)
