from math import ceil


def main():
	w = int(input("A gyémánt magassága:"))
	if w % 2 == 0:
		print("Csak páratlan magasságú gyémánt elfogadott")
		return

	for x in range(w):
		print(('*' * (-2 * abs(x + 1 - ceil((w / 2))) + w)).center(w))


if __name__ == '__main__':
	main()