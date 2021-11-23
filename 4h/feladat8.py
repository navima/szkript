import sys
import random as r

UPTO = 100


def main():
	for i in range(UPTO):
		e = ""
		if (i + 1) % 10 == 0:
			e = "\n"
		print(r.randint(0, 9), end=e)
	print()


main()