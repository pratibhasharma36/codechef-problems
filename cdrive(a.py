t=int(input())
for i in range(t):
	a,b,c,d = list(map(int,input().split()))
	if a > b:
		b=b+c
		if a > b:
			b+=d
			if a<b:
				print("S")
			else:
				print("N")
		else:
			a+=d
			if a>b:
				print("N")
			else:
				print("S")

	elif a<b:
		a+=c
		if a<b:
			a+=d
			if a>b:
				print("N")
			else:
				print("S")
		else:
			b+=d
			if a>b:
				print("N")
			else:
				print("S")
	else:
		print("N")
								