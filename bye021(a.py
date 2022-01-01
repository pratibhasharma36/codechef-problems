t=int(input())
for i in range(t):
	a=int(input())
	b=list(map(int,input().split()))
	l=set()
	for j in b:
		if (j not in l):
			l.add(j)
		else:
			l.add(-j)
	print(len(l))
