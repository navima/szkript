import enum

MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"


class Hangrend(enum.IntFlag):
	SEMMILYEN = 0
	MELY = 1
	MAGAS = 2
	VEGYES = 3


def hangrend(s):
	res = Hangrend(1 & 2)
	for c in s:
		if Hangrend.MELY not in res and c in MELY_MGHK:
			res |= Hangrend.MELY
		if Hangrend.MAGAS not in res and c in MAGAS_MGHK:
			res |= Hangrend.MAGAS
		if Hangrend.MAGAS in res and Hangrend.MELY in res:
			break
	return res


def main():
	print("ablak:", hangrend("ablak").name)
	print("erkély:", hangrend("erkély").name)
	print("kisvasút:", hangrend("kisvasút").name)
	print("magas:", hangrend("magas").name)
	print("mély:", hangrend("mély").name)
	print("Pfffffff:", hangrend("Pfffffff").name)


if __name__ == '__main__':
	main()