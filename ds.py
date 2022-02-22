t=int(input())
for i in range(t):
	s=input()
	count=0
	add=0
	for j in range(len(s)):
		if s[j]=="0":
			count+=1
		else:
			add+=1
	if add<count:
		print(add)
	elif add>count:
		print(count)
	else:
		print(count-1)