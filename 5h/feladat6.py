def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
	u"""Returns text ∩ chars, stable"""
	sb = []
	for c in text:
		if c in chars:
			sb.append(c)
	return "".join(sb)


def main():
	"""The main entry point of the program"""
	print(f'valid("Barking!"): {valid("Barking!")}')
	print(f'valid("KL754", "0123456789"): {valid("KL754", "0123456789")}')
	print(f'valid("BEAN", "abcdefghijklmnopqrstuvwxyz"): {valid("BEAN", "abcdefghijklmnopqrstuvwxyz")}')


if __name__ == '__main__':
	main()