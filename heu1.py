s=input()
ans=0
for i in range(1,len(s)):
	if s[i-1]==s[i]:
		ans=ans+1
print(ans)		
