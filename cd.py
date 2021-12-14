t=int(input())
for i in range(t):
	l,r=input().split()
	l=int(l)
	r=int(r)
	c=0
	a=int(r/2)
	lst=[]
	if l-r>r/2:
		for j in range(l,a):
			c=r%l
			lst.append(c)
			l=l+1
	else:
		for j in range(l,r+1):
			c=r%l
			lst.append(c)
			l=l+1
	print(max(lst))