from palindrome import is_palindrome
from prime import is_prime


def first_prime_palindrome_after(n: int) -> int:
	i = n
	while True:
		if is_palindrome(str(i)) and is_prime(i):
			return i
		i += 1


def main() -> None:
	print(first_prime_palindrome_after(31) == 101)
	print(first_prime_palindrome_after(130) == 131)
	print(first_prime_palindrome_after(131) == 131)
	print(first_prime_palindrome_after(1977) == 10301)


if __name__ == '__main__':
	main()