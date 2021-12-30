t=int(input())
for i in range(t):
	n=int(input())
	s=input()
	if s.find("code")<s.find("chef"):
		print("AC")
	else:
		print("WA")