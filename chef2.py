t=int(input())
for i in range(t):
	n,p,x,y=list(map(int,input().split()))
	a=list(map(int,input().split()))
	ans=0
	
	for i in range(p):
		if a[i]==0:
			ans+=x
		else:
			ans+=y
	print(ans)