def binarize(n):
	num = n
	ress = []
	while not num == 0:
		if num % 2 == 0:
			ress.append('0')
		else:
			ress.append('1')
			num -= 1
		num /= 2
	return "".join(ress)[::-1]


def main():
	print(binarize(156))


if __name__ == '__main__':
	main()