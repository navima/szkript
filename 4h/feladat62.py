MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"


def hangrend(s):
	mely = False
	magas = False
	for c in s:
		if not mely and c in MELY_MGHK:
			mely = True
		if not magas and c in MAGAS_MGHK:
			magas = True
		if magas and mely:
			break
	return mely, magas


def hangrend_to_str(hangrend_tuple):
	if hangrend_tuple[0] and hangrend_tuple[1]:
		return "vegyes"
	if hangrend_tuple[0]:
		return "mely"
	if hangrend_tuple[1]:
		return "magas"
	return "semmilyen"


def main():
	print("ablak:", hangrend_to_str(hangrend("ablak")))
	print("erkély:", hangrend_to_str(hangrend("erkély")))
	print("kisvasút:", hangrend_to_str(hangrend("kisvasút")))
	print("magas:", hangrend_to_str(hangrend("magas")))
	print("mély:", hangrend_to_str(hangrend("mély")))
	print("Pfffffff:", hangrend_to_str(hangrend("Pfffffff")))


if __name__ == '__main__':
	main()