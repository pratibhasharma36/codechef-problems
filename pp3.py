t=int(input())
for i in range(t):
	n=int(input())
	s="abcdefghijklmnopqrstuvwxyz"
	ans=""
	for j in range(n):
		ans = ans + s[j%26]
	print(ans)
