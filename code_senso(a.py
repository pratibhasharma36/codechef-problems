t=int(input())
for i in range(t):
	n=int(input())
	count=0
	for j in range(1,n+1):
		if j%2==0:
			count-=1
		else:
			count+=3
	print(count)