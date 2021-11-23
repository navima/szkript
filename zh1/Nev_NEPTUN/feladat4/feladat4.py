#!/usr/bin/env python3

def main():
	a_n_minus_2 = 1
	a_n_minus_1 = 2
	a_n = a_n_minus_1 + a_n_minus_2
	# print("1, 2, ", end="")
	even_sum = 2
	while a_n < 4000000:
		# print(a_n, end=", ")
		if (a_n % 2) == 0:
			even_sum += a_n

		a_n_minus_2 = a_n_minus_1
		a_n_minus_1 = a_n
		a_n = a_n_minus_1 + a_n_minus_2
	print(even_sum)


if __name__ == '__main__':
	main()