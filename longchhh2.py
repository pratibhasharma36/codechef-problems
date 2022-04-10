for i in range(int(input())):
	x,y,m = list(map(int,input().split()))
	if x*m<y:
		print("yes")
	else:
		print("no")