def genParanthesis(openB, closeB, n, s=[]):

	# base case
	if(closeB == n):
		print("".join(s))
		return

	else:
		if(openB > closeB):
			# you can definitely put one closing bracket
			s.append(')')
			genParanthesis(openB, closeB+1, n , s)
			s.pop()
		if(openB < n):
			s.append('(')
			genParanthesis(openB+1, closeB, n, s)
			s.pop()
	
	return

n = int(input())
genParanthesis(0, 0, n)