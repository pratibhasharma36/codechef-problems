t=int(input())
for i in range(t):
	count=0
	ans=0
	n,m,k=list(map(int,input().split()))
	x=list(map(int,input().split()))
	for i in range(n):
		if x[i]==1:
			count+=1
	if count==n:
		print(100)
	else:
		for j in range(m):
			if x[j]==1:
				ans+=1
		if ans==m:
			print(k)
		else:
			print(0)
