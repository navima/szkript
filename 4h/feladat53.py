def a_xor_b(a, b):
	return bool(a) ^ bool(b)


def main():
	print(f"None xor \"python\" \n= {a_xor_b(None, 'python')}")
	print(f"0 xor \"Null\" \n= {a_xor_b(0, 'Null')}")
	print(f"\"\" xor 0 \n= {a_xor_b('', (0,))}")


if __name__ == '__main__':
	main()