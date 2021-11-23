#!/usr/bin/env python3

import sys


def main():
	if len(sys.argv) != 4:
		print("Hiba! Adj meg pontosan három sztringet!")
	else:
		max_len = max(len(sys.argv[1]), len(sys.argv[2]), len(sys.argv[3]))
		sb = []
		for i in range(max_len):
			for j in range(1, 4):
				if len(sys.argv[j]) - 1 < i:
					sb.append('X')
				else:
					sb.append(sys.argv[j][i])
		print("".join(sb))


if __name__ == '__main__':
	main()