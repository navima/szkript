def main():
	# 1. feladat
	a = []
	with open("string1.py", "r", encoding="utf8") as f_src, open("string1_clean.py", "w", encoding="utf8") as f_dst:
		for line in f_src:
			if not line.startswith("#"):
				f_dst.write(line)
				a.append(line)
	print(a)
	# Finomítás
	f_src = open("string1_clean.py", "r")
	lines = f_src.readlines()
	f_src.close()

	f_dst = open("string1_clean.py", "w")
	for line in lines:
		if not line.lstrip("\t ").startswith('#'):
			print(line, file=f_dst, end="")
	f_dst.close()


if __name__ == '__main__':
	main()