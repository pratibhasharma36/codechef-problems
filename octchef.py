t=int(input())
for i in range(t):
	a,b=list(map(int,input().split()))
	if a>0 and b>0:
		print("Solution")
	elif(a==0):
		print("Liquid")
	elif(b==0):
		print("Solid")