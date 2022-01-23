t=int(input())
for i in range(t):
	x,y,z=list(map(int,input().split()))
	if x>=y:
		print("Pizza")
	elif x>=z:
		print("Burger")
	else:
		print("Nothing")
