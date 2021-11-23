def validate(pos1, pos2, char, s) -> bool:
	return bool((s[pos1-1] == char) ^ (s[pos2-1] == char))


def main():
	acc = 0
	with open("passwords.txt", "r") as f:
		for line in f:
			fields = line.split(" ")
			pos_fields = fields[0].split("-")
			acc += validate(int(pos_fields[0]), int(pos_fields[1]), fields[1][0:-1], fields[2])
	print(acc)


if __name__ == '__main__':
	main()