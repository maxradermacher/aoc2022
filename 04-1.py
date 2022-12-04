import sys

res = 0
for l in sys.stdin:
    r1, r2 = [tuple(int(v) for v in r.split("-")) for r in l.rstrip().split(",")]
    if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
        res += 1
print(res)
