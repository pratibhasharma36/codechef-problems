t=int(input())
for i in range(t):
	x,y,z=list(map(int,input().split()))
	if x+y<=z:
		print("yes")
	else:
		print("no")