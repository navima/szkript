from random import shuffle

from typing import List


def shuffled(li: List) -> List:
	l2 = li[:]
	shuffle(l2)
	return l2


def main() -> None:
	li = [1, 2, 3, 4, 5]
	print(li)
	print(shuffled(li)[-1])
	print(li)


if __name__ == '__main__':
	main()