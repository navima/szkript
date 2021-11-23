from enum import Enum, auto

class EmptyClass:
	pass


class MyClass:
	"""class docstring"""
	"""static variable (class variable/method)"""
	static = 150
	"""static method, @<asd> is a decorator"""

	@staticmethod
	def static_method():
		pass

	"""class method (can refer to callee's class)"""

	@classmethod
	def class_methos(cls):
		pass

	def __init__(self):
		"""pseudo-constructor (called by the constructor)"""
		self.name = "Name not yet generated"

	def hello(self):
		return "hello world!"

	def generate_name(self):
		self.name = "Egy név vagyok"

	def get_name(self):
		return self.name

	def _priv_fun(self):
		"""ez megegyezés szerint privát (amúgy nem az)"""
		pass


obj = MyClass()
print(obj.hello())
print(obj.name)
obj.generate_name()
print(obj.name)


class PSObject:
	pass


obj = PSObject()
obj.name = "dinamikus field"
obj.mane = "nidakisum liefd"
obj.worth = 0
print(obj)


class DerivedClass(MyClass):
	def __init__(self):
		super().__init__()

	def hello(self):
		return "overridden"

	def __str__(self):
		return self.hello() + " + " + super().hello()


obj = DerivedClass()
print(obj.hello())
print(obj)


class Direction(Enum):
	UP = 0
	DOWN = auto()
	LEFT = auto()
	RIGHT = auto()