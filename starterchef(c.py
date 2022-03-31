for i in range(int(input())):
	n,m = list(map(int,input().split()))
	ans = 0
	if n<=m:
		ans = n
		print(ans)
	elif n>=m:
		ans = n*2 - m
		print(ans)
