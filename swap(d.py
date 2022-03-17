for i in range(int(input())):
	n = int(input())
	s = list(input())
	p = sorted(s)
	for j in range(n):
		
		 if s[j] != p[j] and s[j] != p[n-1-j]:
		 	print("no")
		
		 	break
	else:
		print("yes")


