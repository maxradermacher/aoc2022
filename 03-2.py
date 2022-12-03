import string
import sys

res = 0

lines = sys.stdin.read().rstrip().split("\n")
for chunk in [lines[n : n + 3] for n in range(0, len(lines), 3)]:
    (ch,) = set.intersection(*map(set, chunk))
    res += (string.ascii_lowercase + string.ascii_uppercase).index(ch) + 1

print(res)
