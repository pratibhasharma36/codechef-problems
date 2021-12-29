t=int(input())
for i in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	if l[0]!=l[1] and l[1]==l[2]:
		print(1)
	else:
		for j in range(n):
			if l[j]!=l[0]:
				print(j+1)
				break