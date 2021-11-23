#!/usr/bin/env python3

def main():
	while True:
		try:
			szam1 = float(input("1. szam: "))
			szam2 = float(input("2. szam: "))
		except ValueError:
			print("Kerem szamokat adjon meg")
			continue
		try:
			result = szam1 / szam2
		except ZeroDivisionError:
			print("Nullaval osztas!")
			continue
		print('Az osztas eredmenye: {0:.2f}'.format(result))
		print('-' * 10)


#####

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass