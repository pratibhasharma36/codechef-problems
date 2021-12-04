t=int(input())
for _ in range(t):
	n=int(input())
	a= list(map(int,input().split()))
	b=[]
	flag=True
	for i in range(0,n):
		c = a[i] - i
		b.append(c)
	for j in range(n):
		if b[0]!=b[j]:
			flag=False
	if flag==False:
		print(1)
	else:
		print(n)




