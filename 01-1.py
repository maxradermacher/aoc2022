import sys

print(
    max(
        [
            sum([int(val) for val in group.split("\n")])
            for group in sys.stdin.read().rstrip().split("\n\n")
        ]
    )
)
