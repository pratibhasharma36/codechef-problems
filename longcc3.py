t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	count=0
	for j in range(len(a)):
		if a[j]== j+1+count:
			count+=1
	print(count)

