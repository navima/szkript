"""File description"""

nums = [1, 2, 3, 4]
squares = [n * n for n in nums if n >= 2]

if 0 > 3:
	print()
elif 0 > 2:
	print()
else:
	print()

for i, elem in enumerate(nums, start=0):
	if not elem % 2:
		continue
	print(i, elem)
	if not elem % 5:
		break
	else:
		pass


def mult(a, b):
	"""Short description
	long description"""
	return a * b


print(mult(1, 5))
print(mult.__doc__)
help(mult)


def optional_parameters(a, b=1, c=2):
	return a * b * c


optional_parameters(5)
optional_parameters(0, 1)
optional_parameters(1, c=8)