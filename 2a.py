n,x,y=list(map(int,input().split()))
s=input()
l=len(s)
for i in range(l):
	if s[i]=="U":
		y = y+1
	elif s[i]=="D":
		y=y-1
	elif s[i]=="R":
		x=x+1
	elif s[i]=="L":
		x=x-1
print(x,y)