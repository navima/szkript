import random
from typing import Tuple


def _factor_twos(i: int) -> Tuple[int, int]:
	num = i
	s = 0
	d = 0
	while num % 2 == 0:
		s += 1
		num //= 2
	d = num
	if not (2 ** s) * d == i:
		print("bajvan")
	return s, d


def is_prime(i: int) -> bool:
	if i % 2 == 0:
		return False

	rounds = 40
	s, d = _factor_twos(i - 1)

	for _ in range(rounds):
		base = random.randint(2, i - 1)
		x = pow(base, d, i)

		if x == 1 or x == (i - 1):
			continue

		for _ in range(1, s):
			x = pow(x, 2, i)
			if x == (i - 1):
				break
		else:
			return False
	return True


def main() -> None:
	for i in range(2, 30, 2):
		s, d = _factor_twos(i)
		print(f"{i} = {2 ** s} * {d}")

	for i in range(3, 100, 2):
		if is_prime(i):
			print(i)


if __name__ == '__main__':
	main()