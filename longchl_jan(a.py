t=int(input())
for i in range(t):
	t1,t2,r1,r2=list(map(int,input().split()))
	if (t1/t2)**2 == (r1/r2)**3:
		print("yes")
	else:
		print("no")