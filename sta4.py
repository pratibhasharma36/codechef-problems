t=int(input())
for i in range(t):
	n,x=list(map(int,input().split()))
	a=list(map(int,input().split()))
	count=0
	ans=x
	s=x
	for j in range(len(a)):
		ans+=a[j]
		if ans>s:
			s=ans
	print(s)