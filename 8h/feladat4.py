class MyQueue:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []

	def is_empty(self):
		return len(self.in_stack) == 0 and len(self.out_stack) == 0

	def append(self, elem):
		self.in_stack.append(elem)

	def size(self):
		return len(self.in_stack) + len(self.out_stack)

	def popleft(self):
		if len(self.out_stack) == 0:
			if len(self.in_stack) == 0:
				return None
			else:
				while len(self.in_stack) != 0:
					self.out_stack.append(self.in_stack.pop())
				return self.popleft()
		else:
			return self.out_stack.pop()

	def __str__(self):
		return "]" + " ".join([str(elem) for elem in self.out_stack[::-1] + self.in_stack]) + "["


def main():
	q = MyQueue()
	print(q)  # ][
	print(q.is_empty())  # True
	q.append(1)
	q.append(4)
	q.append(5)
	print(q)  # ]1 4 5[
	print(q.size())  # 3
	print(q.is_empty())  # False
	x = q.popleft()
	print(x)  # 1
	print(q)  # ]4 5[
	q.popleft()
	q.popleft()  # most már üres
	x = q.popleft()
	print(x)  # None (jelezzük pl. így, hogy egy üres sorból akarunk kivenni)


if __name__ == '__main__':
	main()