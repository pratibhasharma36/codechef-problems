t=int(input())
for i in range(t):
	x,y=list(map(int,input().split()))
	if x>y and y*2<x:
		print(y)
	else:
		print(int(x/2))