def normalize(s):
	"""Removes whitespace and punctuation, transforms to lower."""
	return s.lower().replace('.','').replace(' ','')


def anagram1(s1, s2):
	"""Returns True if passed in strings are anagrams of each other"""
	a = normalize(s1)
	b = normalize(s2)
	if len(a) != len(b):
		return False

	match_sum = 0
	for c in a:
		if c in b:
			match_sum += 1

	if match_sum == len(a):
		return True
	return False


def anagram2(s1, s2):
	"""Returns True if passed in strings are anagrams of each other"""
	a = normalize(s1)
	b = normalize(s2)
	return sorted(a) == sorted(b)


def main():
	"""The main entry point of the program"""
	print("<A gentleman> <Elegant man> ->", anagram1("A gentleman", "Elegant man"))
	print("<A gentleman> <Elegant man> ->", anagram2("A gentleman", "Elegant man"))


if __name__ == '__main__':
	main()