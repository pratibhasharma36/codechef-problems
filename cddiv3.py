t=int(input())
for i in range(t):
	n=int(input())
	num=1
	count=1
	while count<n:
		num+=1
		if num%3==0:
			num+=1
		if num%10==3:
			num+=1
		if num%3==0:
			num+=1
		count+=1
	print(num)