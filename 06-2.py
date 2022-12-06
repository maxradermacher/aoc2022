import sys

res = 0
for l in sys.stdin:
    for n in range(14, len(l)):
        if len(set(l[n - 14 : n])) == 14:
            print(n)
            break
