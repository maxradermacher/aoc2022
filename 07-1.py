import sys

cwd = []
file_sizes = {}
for l in sys.stdin:
    prefix, _, suffix = l.rstrip().partition(" ")
    if prefix == "$":
        cmd, _, args = suffix.partition(" ")
        if cmd == "cd":
            if args == "/":
                cwd = []
            elif args == "..":
                del cwd[-1:]
            else:
                cwd.append(args)
    elif prefix == "dir":
        pass
    else:
        for n in range(0, len(cwd) + 1):
            dirpath = "/" + "/".join(cwd[:n])
            file_sizes[dirpath] = file_sizes.get(dirpath, 0) + int(prefix)

res = 0
for (dirpath, total) in file_sizes.items():
    if total < 100_000:
        res += total
print(res)
