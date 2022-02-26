for i in range(int(input())):
	a,b,c = list(map(int,input().split()))
	if a+c>=b:
		print(a+c)
	else:
		print(b)