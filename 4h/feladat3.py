def main():
	print(sum(range(101)))
	print((1+100)/2*100)

	n = 0
	for i in range(101):
		for j in str(i):
			n += int(j)

	n2 = sum([sum([int(y) for y in str(x)]) for x in range(101)])

	print(n)
	print(n2)


if __name__ == '__main__':
	main()