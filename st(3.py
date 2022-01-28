t=int(input())
for i in range(t):
	n,k,x=list(map(int,input().split()))
	ans=0
	l=[]
	if k<x:
		print(-1)
	else:
		c = 0
		for j in range(n):
			ans = j%x
			l.append(ans)
	for x in range(len(l)):
		print(l[x],end=" ")
	print()