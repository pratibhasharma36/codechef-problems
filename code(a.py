t=int(input())
for j in range(t):
	n,T=input().split()
	n=int(n)
	T=int(T)
	for i in range(5,T+1):
		if i%5==0:
			n+=n//4
		if i%6==0:
			n-=n//10
	print(n)
			