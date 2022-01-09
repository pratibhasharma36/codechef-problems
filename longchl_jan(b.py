for _ in range(int(input())):
	n,d=input().split()
	n=int(n)
	d=int(d)
	count=1

	if d<=10:
		ans=2**d
		if ans <= n:
			print(ans)
		else:
			print(n)
	else:
		for j in range(10,d):
			ans =1024*(3**count)
			count+=1
			if ans > n:
				break
		if ans <=n :
			print(ans)
		else:
			print(n)