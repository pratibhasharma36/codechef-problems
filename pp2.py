t=int(input())
for i in range(t):
	n,a = list(map(int,input().split()))
	if n-a<=a:
		print(n-a)
	else:
		print(a)