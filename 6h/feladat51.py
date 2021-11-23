def main():
	"""The main entry point of the program"""
	num_sum = 0
	for c in str(2 ** 1000):
		num_sum += int(c)
	print(num_sum)


if __name__ == '__main__':
	main()