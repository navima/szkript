TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

ACCENTED_SUBSTITUTIONS = {
	'á': 'a',
	'é': 'e',
	'í': 'i',
	'ó': 'o',
	'ö': 'o',
	'ő': 'o',
	'ú': 'u',
	'ü': 'u',
	'ű': 'u',
	'Á': 'A',
	'É': 'E',
	'Í': 'I',
	'Ó': 'O',
	'Ö': 'O',
	'Ő': 'O',
	'Ú': 'U',
	'Ü': 'U',
	'Ű': 'U',
}


def main():
	"""The main entry point of the program"""
	for c in TEXT:
		print(ACCENTED_SUBSTITUTIONS.get(c, c), end='')


if __name__ == '__main__':
	main()