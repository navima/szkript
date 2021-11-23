def last_elem(t):
	return t[-1]


def harmadik():
	li = [[2, 6], [1, 3], [5, 4]]
	print(li)
	print(sorted(li, key=last_elem))


def masodik():
	lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

	def extract_id(s: str) -> int:
		return int(s.split(":")[0])

	print(lst)
	print(list(reversed(sorted(lst, key=extract_id))))


def elso():
	data = [
		(1, 'Albany', 'NY', 162692),
		(3, 'Allegany', 'NY', 11986),
		(121, 'Wyoming', 'NY', 8722),
		(123, 'Yates', 'NY', 5094)
	]

	print(list(map(last_elem, data)))
	print(list(map(last_elem, sorted(data, key=last_elem))))


def main():
	elso()
	masodik()
	harmadik()


if __name__ == '__main__':
	main()