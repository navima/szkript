def hello(name, color, obj):
	print("{0}, {1} az {2}!".format(name.capitalize(), color, obj))

if __name__ == '__main__':
	print("{0}, {1} az {2}!".format("geza".capitalize(), "kek", "eg"))

	print(f"1 + 1 = {1 + 1}")

	PI = 3.14159
	print("PI értéke: " + str(PI))
	print("PI értéke: ", PI)

	print("Batman"[2:4])
	print("Batman"[2:])
	print("Batman"[:])
	print("Batman"[-4:-2])
	print("Batman"[::-1])
	print("Batman"[::-2])

	print("""asd
	dsa""")
	print("asd\ndsa")
	print(r"asd\ndsa")

	a = [1, 2, 3]
	b = a[:] #copy
	a == b

	for elem in [2, 3, 4]:
		if elem in a:
			b.append(elem)

	"an" in "batman"