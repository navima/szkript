def main():
	négyzetösszeg = 0
	for i in range(101):
		négyzetösszeg += i ** 2
	összegnégyzet = sum(range(101)) ** 2
	print(abs(összegnégyzet - négyzetösszeg))

if __name__ == '__main__':
	main()