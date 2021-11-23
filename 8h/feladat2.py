class Verem():
	def __init__(self):
		self.l = []

	def __str__(self):
		return "[" + " ".join([str(elem) for elem in self.l])

	def ures(self):
		return len(self.l) == 0

	def betesz(self, elem):
		self.l.append(elem)

	def meret(self):
		return len(self.l)

	def kivesz(self):
		if self.ures():
			return None
		else:
			return self.l.pop()


v = Verem()  # üres verem létrehozása
print(v)  # [
print(v.ures())  # True
v.betesz(1)
v.betesz(4)
v.betesz(5)
print(v)  # [1 4 5
print(v.meret())  # 3
print(v.ures())  # False
x = v.kivesz()
print(x)  # 5
print(v)  # [1 4
v.kivesz()
v.kivesz()  # most már üres
x = v.kivesz()
print(x)  # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


class Sor():
	def __init__(self):
		self.l = []

	def __str__(self):
		return "]" + " ".join([str(elem) for elem in self.l]) + "["

	def ures(self):
		return len(self.l) == 0

	def betesz(self, elem):
		self.l.append(elem)

	def meret(self):
		return len(self.l)

	def kivesz(self):
		if self.ures():
			return None
		else:
			return self.l.pop(0)


s = Sor()
print(s)  # ][
print(s.ures())  # True
s.betesz(1)
s.betesz(4)
s.betesz(5)
print(s)  # ]1 4 5[
print(s.meret())  # 3
print(s.ures())  # False
x = s.kivesz()
print(x)  # 1
print(s)  # ]4 5[
s.kivesz()
s.kivesz()  # most már üres
x = s.kivesz()
print(x)  # None (jelezzük pl. így, hogy egy üres sorból akarunk kivenni)