import sys

score = 0
for line in sys.stdin:
    line = line.rstrip()
    them, _, result = line
    them, result = "ABC".index(them), "XYZ".index(result)
    if result == 0:
        score += ((them + 2) % 3) + 1
    elif result == 1:
        score += 3 + (them + 1)
    elif result == 2:
        score += 6 + ((them + 1) % 3) + 1

print(score)
