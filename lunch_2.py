t=int(input())
for i in range(t):
	a,b,c=list(map(int,input().split()))
	if a+b == c or b+c==a or a+c==b:
		print("yes")
	else:
		print("no")