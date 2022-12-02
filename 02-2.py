import sys

score = 0
for line in sys.stdin:
    them, _, res = line.rstrip()
    them, res = "ABC".index(them), "XYZ".index(res)
    score += 3 * res
    score += (them + res - 1) % 3 + 1

print(score)
