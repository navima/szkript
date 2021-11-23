import sys

def main():
	if len(sys.argv) > 2:
		print(int(sys.argv[1])+int(sys.argv[2]))
	else:
		print("Use: {} (int)A (int)B".format(sys.argv[0]))

if __name__ == '__main__':
	main()