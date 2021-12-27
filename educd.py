t=int(input())
for i in range(t):
	l1,l2,l3 = list(map(int,input().split()))
	if l1==l2+l3 or l2==l1+l3 or l3==l2+l1 :
		print("yes")
	elif (l1 == l2 and l3%2==0) or (l2 == l3 and l1%2==0) or (l3 == l1 and l2%2==0):
		print("yes")
	else:
		print("no") 