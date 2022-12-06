import sys

res = 0
for l in sys.stdin:
    for n in range(4, len(l)):
        if len(set(l[n - 4 : n])) == 4:
            print(n)
            break
