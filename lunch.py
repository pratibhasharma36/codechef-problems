t=int(input())
for i in range(t):
	d,l,r=list(map(int,input().split()))
	if d>=l and d<=r:
		print("Take second dose now")
	elif d<=l and d<=r:
		print("Too Early")
	elif d>=l and d>=r:
		print("Too Late")