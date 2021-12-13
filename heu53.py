n=int(input())
eve=0
odd=0
while n!=0:
	num=int(n%10)
	if num%2==0:
		eve=eve+num
	else:
		odd=odd+num
	n=n/10
print(eve,end=" ")
print(odd)