for i in range(int(input())):
	a,b = list(map(int,input().split()))
	l = list(map(int,input().split()))
	l.sort()
	add = 0
	count=0
	

	for j in range(1,len(l)+1):
		add = add + l[-j]
		count+=1
		if add >= b:
			break
		else:
			continue
	print(len(l)-count)
	

