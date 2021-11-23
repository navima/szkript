words = ["ccc", "aaaa", "d", "bb"]
sorted(words)
sorted(words, key=len)
sorted(words, key=str.lower)
def last_char(s: str) -> str:
	return s[-1]
sorted(words, key=last_char)


try:
	f = open("asd", "r")
	f.read()
except (IOError, KeyboardInterrupt) as e:
	print(e)