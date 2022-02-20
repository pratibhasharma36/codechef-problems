t=int(input())
for i in range(t):
	n,x,y=list(map(int,input().split()))
	l = []
	ans=0
	for j in range(n+1):
		car = j // 4
		if j % 4 != 0:
			car += 1
		bus = (n - j) // 100
		if (n-j) % 100 != 0:
			bus += 1
		ans = car * y + bus * x
		l.append(ans)
	print(min(l))




