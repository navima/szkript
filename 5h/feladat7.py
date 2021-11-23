def main():
	"""The main entry point of the program"""
	for i in range(438579089):
		nsum = 0
		for c in str(i):
			if c == '0':
				continue
			nsum += pow(int(c), int(c))
			if nsum > i:
				break
		if nsum == i:
			print("n=", i)


if __name__ == '__main__':
	main()