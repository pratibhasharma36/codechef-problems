t=int(input())

for j in range(t):
	lst=[]
	 
	a1,a2,a3,a4,a5,a6,a7 = list(map(int,input().split()))
	
	lst.append(a1)
	lst.append(a2)
	lst.append(a3)
	lst.append(a4)
	lst.append(a5)
	lst.append(a6)
	lst.append(a7)
	count=0
	ans=0
	for i in range(len(lst)):
		if lst[i]== 1:
			count+=1
		else:
			ans+=1
	
		
	if count>ans:
		print("yes")
	else :
		print("no")
