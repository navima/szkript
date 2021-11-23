def print_board(l):
	"""Prints a chessboard of arbitrary size, filled with Queens at specified positions."""
	l_transposed = l[:]
	for i, elem in enumerate(l):
		l_transposed[elem] = i
	l_transposed.reverse()

	print('+' + '-' * 17 + '+')
	for elem in l_transposed:
		print("| " + ". " * elem + "Q " + ". " * (len(l) - elem - 1)+"|")
	print('+' + '-' * 17 + '+')


def main():
	"""The main entry point of the program"""
	print_board([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == '__main__':
	main()