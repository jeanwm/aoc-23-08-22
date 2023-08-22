def f(abc):
	A = ((abc & 4) >> 2) == 1
	B = ((abc & 2) >> 1) == 1
	C = ((abc & 1)) == 1
	return (not A or C) and (A or C or B) and not B
	
for abc in range(8):
	print(str((abc & 4) >> 2) + " ", end="")
	print(str((abc & 2) >> 1) + " ", end="")
	print(str((abc & 1)) + " ", end="")
	print(str(f(abc)))
