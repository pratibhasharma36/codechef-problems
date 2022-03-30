for i in range(int(input())):
	n,m,k = list(map(int,input().split()))
	if n+k<=m:
		print("yes")
	else:
		print("no")
