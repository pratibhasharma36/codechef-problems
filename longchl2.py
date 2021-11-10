t=int(input())
for i in range(t):
	x,y=input().split()
	x=int(x)
	y=int(y)
	if (x*1 + y*2)%2==0:
		if x==0 and y%2!=0:
			print("NO")
		else:
			print("YES")
	else:
		print("NO")