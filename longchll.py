t=int(input())
for i in range(t):
	f,s,t=map(str,input().split())

	x,y=input().split()
	if (x==f and y==s):
		print(x)
	elif (x==f and y==t):
		print(x)
	elif (x==s and y==f):
		print(y)
	elif (x==s and y==t):
		print(y)
	elif (x==t and y==f):
		print(y)
	elif (x==t and y==s):
		print(y)
