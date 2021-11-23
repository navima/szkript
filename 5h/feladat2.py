def loop(n, debug=False):
	"""Prints numbers 1-n (incl.) separated with spaces.
	Call with debug=True to print debug information (loop start/end)"""
	if debug:
		print("# ciklus kezdete:")
	for i in range(n):
		if i != 0:
			print(" ", end="")
		print(i + 1, end="")
	print()
	if debug:
		print("# ciklus vége")


def main():
	"""The main entry point of the program."""
	loop(5)
	loop(5, debug=True)


if __name__ == '__main__':
	main()