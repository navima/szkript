def test(l):
	"""Returns Median of passed-in list"""
	if len(l) % 2:
		return sorted(l)[len(l) // 2]
	else:
		return (sorted(l)[len(l) // 2] + sorted(l)[len(l) // 2 - 1]) / 2


def main():
	"""The main entry point of the program"""
	print(test([1, 2, 3, 4, 5]) == 3)
	print(test([3, 1, 2, 5, 3]) == 3)
	print(test([1, 300, 2, 200, 1]) == 2)
	print(test([3, 6, 20, 99, 10, 15]) == 12.5)


if __name__ == '__main__':
	main()