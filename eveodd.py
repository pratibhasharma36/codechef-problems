t=int(input())
for i in range(t):
	n=int(input())
	count=0
	ans=0
	for j in range(n):
		if j**2<n:
			count+=1
		elif j**3<=n:
			ans+=1
	print(ans+count)