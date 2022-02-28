for _ in range(int(input())):
	n,k = map(int,input().split())
	a= list(map(int,input().split()))
	l=len(a)
	m = []
	for k in range(a[0],0,-1):
		m.append(k)
	for i in range(l):
		for j in range(a[i],a[i-1],-1):
			m.append(j)

	print(*m)


