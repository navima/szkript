def main():
	with open("szoveg.txt", "r") as f:
		for line in f:
			sb = []
			for word in line.split():
				if word[::-1] == word:
					sb.append(word)
				else:
					sb.append("X" * len(word))
			print(" ".join(sb))


if __name__ == '__main__':
	main()