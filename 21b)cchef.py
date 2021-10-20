t=int(input())
for i in range(t):
	x,y = map(int,input().split())
	st=input()
	l=[]
	li=[-1]
	count=0
	for j in range(len(st)):
		l.append(st[j])

	for i in range(len(l)):
		if l[i]=="1":
			count+=1
		else:
			li.append(i)
	
	streak = 0

	for k in range(len(li)-1):
		streak=max(streak, li[k+1]-li[k]-1)
	if len(li) != 0:
		streak=max(streak, len(l) - li[-1]-1)
	print(count*x+streak*y)
