def egy(in_list):
	"""
	Transforms each element of input to uppercase and appends an exclamation mark.
	:param in_list: the input list
	:type in_list: list of string
	:return: the transformed string
	:rtype: list of string
	"""
	return [s.upper() + '!' for s in in_list]


def ketto(in_list):
	"""
	Capitalizes every string in input.
	:param in_list: the input list
	:type in_list: list of string
	:return: the capitalized string
	:rtype: list of string
	"""
	return [s.capitalize() for s in in_list]


def harom():
	"""
	Creates a 10 long list of zeros (int).
	:return: the created list
	:rtype: list of int
	"""
	return [0 for _ in range(10)]


def negy(in_list):
	"""
	Multiplies every element of input by 2.
	:param in_list: the input list
	:type in_list: list of int
	:return: a new list of the modified members
	:rtype: list of int
	"""
	return [n * 2 for n in in_list]


def ot(in_list):
	"""
	Calls int on each element of input.
	:param in_list: the input list
	:type in_list: list of string
	:return: a new list containing the parsed results
	:rtype: list of int
	"""
	return [int(n) for n in in_list]


def hat(s):
	"""
	Creates a list of the characters of the input string converted to int.
	:param s: the input string
	:type s: string
	:return: a new list containing the parsed results
	:rtype: list of int
	"""
	return [int(c) for c in s]


def het(s):
	"""
	Creates a list containing the lengths of whitespace-delimited substrings of input.
	:param s: the input string
	:type s: string
	:return: a new list containing the lengths of the substrings
	:rtype: list of int
	"""
	return [len(substring) for substring in s.split()]


def nyolc(s):
	"""
	Creates a list containing the first character of whitespace-delimited substrings of input.
	:param s: the input string
	:type s: string
	:return: a new list containing the first character of the substrings
	:rtype: list of string
	"""
	return [substring[0] for substring in s.split()]


def kilenc(s):
	"""
	Creates a list of tuples in the form of (substring, length), describing whitespace-delimited substrings of input.
	:param s: the input string
	:type s: string
	:return: the list of tuples
	:rtype: list of tuple of string, int
	"""
	return [(substring, len(substring)) for substring in s.split()]


def tiz():
	"""
	Creates a list containing all even natural numbers (incl. 0) less than 10.
	:return: the list of numbers
	:rtype: list of int
	"""
	return [i for i in range(10) if not i % 2]


def tizenegy():
	"""
	Creates a list of all even squares of [natural numbers (incl. 0) less than 20].
	:return: the list of numbers
	:rtype: list of int
	"""
	return [i ** 2 for i in range(20) if not i ** 2 % 2]


def tizenketto():
	"""
	Creates a list of all '4'-postfixed squares of [natural numbers (incl. 0) less than 20].
	:return: the list of numbers
	:rtype: list of int
	"""
	return [i ** 2 for i in range(20) if str(i ** 2)[-1] == '4']


def tizenharom():
	"""
	Creates a string of every character with Unicode code between that of 'A' and 'Z'.
	:return: the resulting string
	:rtype: string
	"""
	return "".join([chr(i) for i in range(ord('A'), ord('Z') + 1)])


def tizennegy(in_list):
	"""
	Calls strip on each element of input.
	:param in_list: the input list
	:type in_list: list of string
	:return: new list of transformed strings
	:rtype: list of string
	"""
	return [s.strip() for s in in_list]


def tizenot(in_list):
	"""
	Creates a string containing each element of input transformed to string and concatenated.
	:param in_list: the input list
	:type in_list: list of int
	:return: resulting string
	:rtype: string
	"""
	return "".join([str(n) for n in in_list])


# ------------------------------------------------------------------------------
RESET = '\033[0m'
BOLD = '\033[01m'
RED = '\033[31m'
GREEN = '\033[32m'


def test(fn, fn_input, fn_expected_output):
	"""
	Calls the passed function like so: fn( fn_input ), and compares result with supplied expected output.
	Input and output must support ==.
	:param fn: the function to call
	:param fn_expected_output: arbitrary output
	:param fn_input: arbitrary input
	:return: Nothing
	"""

	if fn_input is None:
		res = fn()
	else:
		res = fn(fn_input)

	print(BOLD + GREEN + "OK " + RESET if res == fn_expected_output else BOLD + RED + "X  " + RESET, end="")
	print(f"- expected: {fn_expected_output}\n          got: {res}")


def main():
	"""The main entry point of the program"""
	test(egy, ['auto', 'villamos', 'metro'], ['AUTO!', 'VILLAMOS!', 'METRO!'])
	test(ketto, ['aladar', 'bela', 'cecil'], ['Aladar', 'Bela', 'Cecil'])
	test(harom, None, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	test(negy, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
	test(ot, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	test(hat, "1234567", [1, 2, 3, 4, 5, 6, 7])
	test(het, 'The quick brown fox jumps over the lazy dog', [3, 5, 5, 3, 5, 4, 3, 4, 3])
	test(nyolc, "python is an awesome language", ['p', 'i', 'a', 'a', 'l'])
	test(kilenc, 'The quick brown fox jumps over the lazy dog',
	     [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4),
	      ('dog', 3)])
	test(tiz, None, [0, 2, 4, 6, 8])
	test(tizenegy, None, [0, 4, 16, 36, 64, 100, 144, 196, 256, 324])
	test(tizenketto, None, [4, 64, 144, 324])
	test(tizenharom, None, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	test(tizennegy, [' apple ', ' banana ', ' kiwi'], ['apple', 'banana', 'kiwi'])
	test(tizenot, [1, 0, 1, 1, 0, 1, 0, 0], "10110100")


if __name__ == '__main__':
	main()