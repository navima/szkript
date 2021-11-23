t = [1, 2, 3, 4, 3, 2, 1]
a = set(t)
1 in a
b = set()
b.add(1)
b.add(1)
b.add(2)
b.union(a)
b.intersection(a)
b.difference(a)
b.remove(1)

d = {}
d['a'] = 1
d[1] = "rekt"
print(d)
d[1]
d.get(1)
d.get("lol", "def")
1 in d
d.keys()
d.values()
for k in sorted(d.keys()):
	print(k, ": ", d[k])
d.items()
for k, v in d.items():
	print(k, ": ", v)
del d[1]
zip([1, 2, 3], [9, 8, 7])