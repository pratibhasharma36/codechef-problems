t=int(input())
for i in range(t):
	a1,b1,c1=list(map(int,input().split()))
	a2,b2,c2=list(map(int,input().split()))
	tot1=a1+b1+c1
	tot2=a2+b2+c2
	if tot1>tot2:
		print("Dragon")
	if tot1==tot2:
		if a1>a2:
			print("Dragon")
		elif a1==a2:
			if b1>b2:
				print("Dragon")
			elif b1<b2:
				print("Sloth")
			else:
				print("Tie")
		else:
			print("Sloth")
	if tot1<tot2:
		print("Sloth")