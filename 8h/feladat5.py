def main():
	diffs = []
	with open("day02.txt", "r") as f:
		for line in f:
			strs = line.split()
			nums = [int(elem) for elem in strs]
			diffs.append(max(nums)-min(nums))
	print(sum(diffs))

if __name__ == '__main__':
	main()