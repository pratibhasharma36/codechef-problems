t=int(input())
for i in range(t):
	n=int(input())
	s=input()
	count=0
	for i in range(len(s)):
		for j in range(i+1,min(n,i+10)):
			if j-i==abs(int(s[j])-int(s[i])):
				count+=1
	print(count)