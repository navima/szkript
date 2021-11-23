#!/usr/bin/env python3

import math


def main():
	with open("input.txt", "r") as f:
		square_elems_dict = {}
		for line in f:
			elems = line.split(";")
			key = int(elems[0])
			if pow(math.floor(math.sqrt(key)), 2) == key:
				square_elems_dict[key] = elems[1]
		sb = []
		for key in sorted(square_elems_dict.keys()):
			sb.append(square_elems_dict[key][0])
		print("".join(sb).replace("_", " "))


if __name__ == '__main__':
	main()