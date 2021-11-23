import locale


header = ("Fibonacci n", 30, 40, 50, 5000)
data = [
	("Racket", 22, 2673, 335343, -1),
	("Haskell (compiled O3)", 195, 3277, 457965, -1),
	("C++ (MSVC)", 6, 787, 94530, -1),
	("C++ (MSVC Release)", 2, 303, 37435, -1),
	("C++ (WSL g++)", 5, 639, 68581, -1),
	("C#", 6, 708, 87176, -1),
	("C# (caching)", 0, 0, 0, 3)
]


def main():
	locale.setlocale(locale.LC_ALL, '')

	fh = "{:>25} | {:^9} | {:^9} | {:^9} | {:^9}"
	fd = "{:.<25} | {:>9n} | {:>9n} | {:>9n} | {:>9n}"
	print(fh.format(header[0], header[1], header[2], header[3], header[4]))
	print(f"{header[0]:>25} | {header[1]:^9} | {header[2]:^9} | {header[3]:^9} | {header[4]:^9}")

	print("-" * len(fd.format(0, 0, 0, 0, 0)))
	for elem in data:
		print(fd.format(elem[0], elem[1], elem[2], elem[3], elem[4]))


if __name__ == '__main__':
	main()