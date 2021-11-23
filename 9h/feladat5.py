from palindrome import is_palindrome


def main() -> None:
	i_sum = 0
	for i in range(1000000):
		if is_palindrome(str(i)) and is_palindrome(f"{i:b}"):
			print(f"{i}, {i:b}")
			i_sum += i
	print(i_sum)


if __name__ == '__main__':
	main()