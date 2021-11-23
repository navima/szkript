s = "asd dsa djrhz"
l = ["a", "b", "s"]
print(s.split(" "))
print(", ".join(l))
rfrom = 0
rto = 20
rstep = 2
print(range(rfrom, rto, rstep))
print(list(range(rfrom, rto, rstep)))
print(bool(None))
print(bool("asd"))
# stringbuilder = "".join([<string>, ...])
a = 1
b = 5
a, b = b, a
(a, b) = (b, a)
def getstuff(): return (1, 2, 'a')
(egy, ketto, harom) = getstuff()	#value unpacking
a, b, c = getstuff()	#value unpacking