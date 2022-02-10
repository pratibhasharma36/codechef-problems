t=int(input())
for i in range(t):
	n=int(input())
	l=[]
	m=[]
	count=0
	for j in range(n):
		x,y=list(map(int,input().split()))
		l.append(x)
		m.append(y)
	l=set(l)
	
	m=set(m)
	print(len(m)+len(l))
