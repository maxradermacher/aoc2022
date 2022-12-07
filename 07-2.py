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

available_space = 70_000_000 - file_sizes["/"]
required_space = 30_000_000
size_to_delete = required_space - available_space

for size in sorted(file_sizes.values()):
    if size >= size_to_delete:
        print(size)
        break
