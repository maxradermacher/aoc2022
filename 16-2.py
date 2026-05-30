import sys

i = {}
v = []
for l in sys.stdin:
	c = l.split(" ")
	name, rate, tunnels = c[1], int(c[4][5:-1]), list(map(lambda v: v[:-1], c[9:]))
	i[name] = len(v)
	v.append((rate, tunnels))

v = list([(r, list(map(lambda name: i[name], t))) for (r, t) in v])

res = 0
stack = [(0, 26, i["AA"], i["AA"], 0)]
b = {}
t = 0
n = 0
while len(stack) > 0:
	n += 1
	total, time, you, ele, opened = stack.pop(0)
	if n % 100_000 == 0:
		print(time, n)
	res = max(res, total)
	if time == 1:
		break
	key = (1 << you | 1 << ele, opened)
	if total <= b.get(key, -1):
		continue
	b[key] = total

	inter = []
	final = []

	rate, tunnels = v[you]
	if (opened & (1 << you)) == 0 and rate > 0:
		inter.append((total + (time - 1) * rate, you, opened | 1 << you))
	for tunnel in tunnels:
		inter.append((total, tunnel, opened))

	rate, tunnels = v[ele]
	for (total, you, opened) in inter:
		if (opened & (1 << ele)) == 0 and rate > 0:
			final.append((total + (time - 1) * rate, time - 1, you, ele, opened | 1 << ele))
		for tunnel in tunnels:
			final.append((total, time - 1, you, tunnel, opened))

	stack.extend(final)


print(n, res)