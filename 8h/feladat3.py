PI = 3.1415926535898


class Sphere:
	def __init__(self, radius):
		self.r = radius

	def volume(self):
		return 4 * PI * pow(self.r, 3) / 3

	def surface(self):
		return 4 * PI * pow(self.r, 2)

	def __lt__(self, other):
		return self.r < other.r

	def __le__(self, other):
		return self.r <= other.r

	def __gt__(self, other):
		return self.r > other.r

	def __ne__(self, other):
		return self.r >= other.r


class Ellipse:
	def __init__(self, major, minor):
		self.major = major
		self.minor = minor

	def area(self):
		return PI * self.minor / 2 * self.major / 2


def main():
	s1 = Sphere(10)
	print(s1.volume())
	print(s1.surface())
	print(s1.r)
	s2 = Sphere(10)
	print(s1 < s2)
	print(s1 <= s2)
	print(s1 > s2)
	print(s1 >= s2)

	e = Ellipse(20, 10)
	print(e.area())
	print(e.major)
	print(e.minor)


if __name__ == '__main__':
	main()