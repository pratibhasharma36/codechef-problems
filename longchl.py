t=int(input())
for i in range(t):
	x,y,a,b,k=list(map(int,input().split()))
	if (x+k*a) < (y+k*b):
		print("PETROL")
	elif (x+k*a) > (y+k*b):
		print("DIESEL")
	else:
		print("SAME PRICE")
	