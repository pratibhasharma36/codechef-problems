lst=list(map(int,input().split()))
newls=[]
l=len(lst)
for i in range(l+1):
	for j in range(i):
		newls.append(lst[j:i])
print(newls)