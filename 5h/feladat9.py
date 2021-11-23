def main():
	"""The main entry point of the program"""
	s = input()
	prev = s[-1]
	numsum = 0
	for c in s:
		if c == prev:
			numsum += int(c)
		prev = c
	print(numsum)


if __name__ == '__main__':
	main()