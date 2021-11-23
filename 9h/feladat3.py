from typing import List


def parse_page_notation(in_str: str) -> List[int]:
	in_lst = in_str.split(",")
	out_lst = []
	for elem in in_lst:
		if "-" in elem:
			elem_elems = elem.split("-")
			out_lst += list(range(int(elem_elems[0]), int(elem_elems[1])+1))
		else:
			out_lst.append(int(elem))
	return out_lst


def main() -> None:
	in_str = input("Nyomtatandó oldalak: ")
	print(parse_page_notation(in_str))


if __name__ == '__main__':
	main()