t=int(input())
for i in range(t):
	x,y=list(map(int,input().split()))
	if x<y:
		print("Bike")
	elif x>y:
		print("Car")
	else:
		print("Same")