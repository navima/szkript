#!/usr/bin/env python3

def brace_counter(s):
	counter = 0
	max_counter = 0
	min_counter = 0
	counter_vals = {0: 1}
	for c in s:
		if c == "(":
			counter += 1
		else:
			counter -= 1
		if counter > max_counter:
			max_counter = counter
		if counter < min_counter:
			min_counter = counter
		counter_vals[counter] = counter_vals.get(counter, 0) + 1
	return (counter, max_counter, min_counter, counter_vals)


def main():
	s = ""
	with open("input.txt", "r") as f:
		s = f.readline()
	res, max_floor, min_floor, touched_floors = brace_counter(s)
	print("Cél emelet:", res)
	print("Legmagasabb emelet:", max_floor)
	print("Legmélyebb emelet:", min_floor)
	touched_floor_max = 0, 1
	for k, v in touched_floors.items():
		if touched_floor_max[1] < v:
			touched_floor_max = (k, v)
	print("Legtöbbször érintett emelet:", touched_floor_max[0])


if __name__ == '__main__':
	main()