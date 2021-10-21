t=int(input())
for i in range(t):
	x,y=list(map(int,input().split()))
	if abs(x-y)%2==0:
		print("yes")
	else:
		print("no")