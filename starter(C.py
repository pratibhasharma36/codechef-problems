for i in range(int(input())):
	k=int(input())
	ans=0
	count=0
	for j in range(1,k):
		if k%(2**j)==0 :
			count+=1
		else:
			break
	print(count)
