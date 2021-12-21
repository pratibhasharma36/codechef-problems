for i in range(int(input())):
	s=input()
	n=len(s)
	if n%2!=0 :
		print("No")
	else:
		s1 = s[:n//2]
		s2 = s[n//2:]
		flag = True
		for j in range(n//2):
			if s1[j]!= s2[j]:
				flag= False
				break
		if flag:
			print("Yes")
		else:
			print("No")