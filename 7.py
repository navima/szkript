import sys
import shutil

G_CONSTANT = 0
g_var = 0
def f():
	global g_var
	g_var = 1560
f = open("asd.txt", "r") # r w a
for line in f:
	a = line.rstrip("\n")
	print(line, end="") # a \n-t is beolvassa
f.seek(0)
lines = f.readlines() # list of string
f.seek(0)
read_to_end = f.read()
f.seek(0)
lines = f.read().splitlines()
f.close()

f = open("dsa.txt", "w")
f.write("111\n")
print("222\n", file=f)
print("err", file=sys.stderr)
f.close()
with open("asd.txt","r") as f1, open("dsa.txt", "w") as f2:
	pass
	# f1.close()
	# f2.close()
# shutil.copy("f1", "f2")