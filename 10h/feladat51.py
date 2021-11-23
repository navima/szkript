import re
import csv


def main():
	with open("DT2.csv", "r", newline='') as f:
		for line in csv.reader(f):
			if re.match(".*j.*s.*u.*n.*", line[0]):
				print(line[0])


if __name__ == '__main__':
	main()