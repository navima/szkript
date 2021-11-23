import sys


def double_digits(text:str) -> str:
	sb = []
	for c in text:
		if c in "0123456789":
			sb.append(c)
		sb.append(c)
	return "".join(sb)


def main() -> None:
	if not len(sys.argv) == 2:
		print("Hibás paraméterezés! Egyetlen sztringet kell megadni!")
		return
	print(double_digits(sys.argv[1]))


if __name__ == '__main__':
	main()