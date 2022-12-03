import sys

result = 0

uniq = []
for line in sys.stdin:
    uniq.append(set(line.rstrip()))
for idx in range(0, len(uniq), 3):
    (v,) = uniq[idx].intersection(uniq[idx+1]).intersection(uniq[idx+2])
    if ord(v) >= ord("a"):
        result += ord(v) - ord("a") + 1
    else:
        result += ord(v) - ord("A") + 1 + 26

print(result)
