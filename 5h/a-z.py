import sys


def main():
	"""The main entry point of the program"""
	if "z-a" in sys.argv[0]:
		print("".join([chr(i) for i in range(ord('a'), ord('z') + 1)][::-1]))
	else:
		print("".join([chr(i) for i in range(ord('a'), ord('z') + 1)]))


if __name__ == '__main__':
	main()