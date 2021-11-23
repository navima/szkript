from itertools import combinations
from math import prod


def factors(x, limit=-1):
	if limit == -1:
		limit = x
	return [i for i in range(1, limit + 1) if not x % i]


def calc_hatoslotto(digits_sum, digits_product):
	digits = factors(digits_product, limit=45)
	for combination in combinations(range(len(digits)), 6):
		nums = [digits[j] for j in combination]
		if sum(nums) == digits_sum and prod(nums) == digits_product:
			return nums
	return None

	# Csak általunk már használt eszközökkel:
	#for a in range(0, len(digits)):
	#	for b in range(a + 1, len(digits)):
	#		for c in range(b + 1, len(digits)):
	#			for d in range(c + 1, len(digits)):
	#				for e in range(d + 1, len(digits)):
	#					for f in range(e + 1, len(digits)):
	#						if digits[a] + digits[b] + digits[c] + digits[d] + digits[e] + digits[f] == digits_sum \
	#								and digits[a] * digits[b] * digits[c] * digits[d] * digits[e] * digits[f] == digits_product:
	#							return [digits[a], digits[b], digits[c], digits[d], digits[e], digits[f]]
	#return None


def main():
	print(calc_hatoslotto(90, 996300))


if __name__ == '__main__':
	main()