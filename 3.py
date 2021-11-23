import sys
from collections import deque

if __name__ == '__main__':
	sys.stdout.write("asd")
	sys.stdout.write("dsa\n")

	a = [1, 2, 3]
	a.append(4)
	print(a.pop())
	print(a.pop(1))
	del a[1]
	a.insert(1, 5)
	sorted(a, reverse=False)
	a.sort(reverse=True)
	max(a)
	min(a)
	sum(a)

	q = deque([1, 2, 3])
	q.append(4)
	q.popleft()