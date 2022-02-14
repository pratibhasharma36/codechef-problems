t=int(input())
for i in range(t):
	n,x = list(map(int,input().split()))
	ans=0
	print(x % (n + 1))

