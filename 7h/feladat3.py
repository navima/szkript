BRACE_PAIRS = {
	"]": "[",
	")": "(",
	"}": "{"
}


def test(s):
	stack = []
	for c in s:
		if c == "[" or c == "{" or c == "(":
			stack += c
		elif c == "]" or c == "}" or c == ")":
			if stack.pop() != BRACE_PAIRS[c]:
				return False
	return not len(stack)


def main():
	print(test("((5+3)*2+1)") == True)
	print(test("{[(3+1)+2]+}") == True)
	print(test("(3+{1-1)}") == False)
	print(test("[1+1]+(2*2)-{3/3}") == True)
	print(test("(({[(((1)-2)+3)-3]/3}-3)") == False)


if __name__ == '__main__':
	main()