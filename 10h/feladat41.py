def main():
	cell_num = 600
	cells = [True] * cell_num
	for i in range(2, cell_num + 1):
		for k in range(i - 1, cell_num, i):
			cells[k] = not cells[k]

	open_cells = []
	for i in range(cell_num):
		if cells[i]:
			open_cells.append(i + 1)
	print("nyitott cellák:", open_cells)


if __name__ == '__main__':
	main()