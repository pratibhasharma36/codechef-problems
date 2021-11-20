n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
	if l[i]%2==0:
		a+=1
	else:
		b+=1
count=(a*(a-1))/2
add=(b*(b-1))/2
s=int(count+add)
print(s)