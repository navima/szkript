import csv


def main():
	with open("numbers.csv", "r", newline='') as f:
		reader = csv.reader(f, delimiter=';')
		sum_hun = 0.0
		count_hun = 0
		sum_eng = 0.0
		count_eng = 0
		for row in reader:
			for col in row[0:3]:
				if "." in col:
					sum_eng += float(col)
					count_eng += 1
				else:
					sum_hun += float(col.replace(",", "."))
					count_hun += 1
		print(f"""A fájlban {count_eng} db angol és {count_hun} db magyar szám található.
Angol számok öszege: {round(sum_eng, 2)}
Magyar számok összege: {round(sum_hun, 2)}""")


if __name__ == '__main__':
	main()