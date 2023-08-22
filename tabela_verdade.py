def f(abc):
	A = ((abc & 4) >> 2) == 1
	B = ((abc & 2) >> 1) == 1
	C = ((abc & 1)) == 1

	# Z = (A'+C)(A+C+B)B' = B'C	
	# return (not A or C) and (A or C or B) and not B
	
	# Z = (A'B'C')+(A'B'C)+(A'BC')+(AB'C')+(ABC')+(ABC)	
	r = not A and not B and not C
	r = r or (not A and not B and C)
	r = r or (not A and B and not C)
	r = r or (A and not B and not C)
	r = r or (A and B and not C)
	r = r or (A and B and C)
	return r
	
for abc in range(8):
	print(str((abc & 4) >> 2) + " ", end="")
	print(str((abc & 2) >> 1) + " ", end="")
	print(str((abc & 1) >> 0) + " ", end="")
	print(str(f(abc)))
