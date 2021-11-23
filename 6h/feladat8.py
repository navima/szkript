import sys

def main():
	"""The main entry point of the program"""
	correct_sum = 0
	for line in sys.stdin:
		words = line.split()
		if len(set(words)) == len(words):
			correct_sum += 1
	print(correct_sum)


if __name__ == '__main__':
	main()