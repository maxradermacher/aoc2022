import sys

result = 0
for line in sys.stdin:
    line = line.rstrip()
    half = len(line)//2
    print(line[:half], line[half+1:])
    h1, h2 = set(line[:half]), set(line[half:])
    print(line)
    (v,) = h1.intersection(h2)
    if ord(v) >= ord("a"):
        result += ord(v) - ord("a") + 1
    else:
        result += ord(v) - ord("A") + 1 + 26

print(result)
