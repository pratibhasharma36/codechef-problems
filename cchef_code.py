t=int(input())
for i in range(t):
	n=int(input())
	s=input()
	l=[]
	flag=0
	for j in range(len(s)):
		l.append(s[j])
	for k in range(len(l)-1):
		if l[k]==l[k+1]:
			flag=1
			break
	if flag==1:
		print("yes")
	else:
		print("no")
