t=int(input())
for i in range(t):
	s,v=list(map(str,input().split()))
	count=0
	for j in range(len(v)-1):
		if s[0:3]==v[j:j+3] :
			count+=1
	print(count)

