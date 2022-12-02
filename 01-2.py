import sys

print(
    sum(
        sorted(
            [
                sum([int(val) for val in group.split("\n")])
                for group in sys.stdin.read().rstrip().split("\n\n")
            ]
        )[-3:]
    )
)
