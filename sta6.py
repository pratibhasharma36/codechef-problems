t=int(input())
for i in range(t):
	n=int(input())
	b=list(map(int,input().split()))
	l=[]
	m=[]
	for j in range(len(b)):
		if b[j]%2==0:
			l.append(b[j])
		else:
			m.append(b[j])
	if len(l)%2==0 and len(m)%2==0:
		print("yes")
	else:
		print("no")
