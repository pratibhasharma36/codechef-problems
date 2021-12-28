t=int(input())
for i in range(t):
	a,b,c=list(map(int,input().split()))
	a1=int(a)*1
	b1=int(b)*2
	c1=int(c)*3
	sum=a1+b1+c1
	print(sum%2)