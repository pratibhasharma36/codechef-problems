t=int(input())
for i in range(t):
	n,x,y=list(map(int,input().split()))
	if (n+1)*y>=x:
		print("yes")
	else:
		print("no")