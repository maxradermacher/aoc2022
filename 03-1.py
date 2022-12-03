import string
import sys

res = 0

for line in sys.stdin.read().rstrip().split("\n"):
    half = len(line) // 2
    h1, h2 = set(line[:half]), set(line[half:])
    (ch,) = h1.intersection(h2)
    res += (string.ascii_lowercase + string.ascii_uppercase).index(ch) + 1

print(res)
