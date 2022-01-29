t=int(input())
for i in range(t):
	n,x,y=list(map(int,input().split()))
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	l=[]
	for j in range(len(a)):
		if a[j]+x==b[j] or a[j]+y==b[j]:
			l.append(a[j])
	if a == l:
		print("yes")
	else:
		print("no")