for i in range(int(input())):
	n=int(input())
	if n>65:
		print("Overload")
	elif n<=65 and n>=35:
		print("Normal")
	else:
		print("Underload")