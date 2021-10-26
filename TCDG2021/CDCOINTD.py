#https://www.codechef.com/TCDG2021/problems/CDCOINTD/
testcases = int(input())
for test in range (0, testcases):
    a, b, c, d = map(int, input().split())
    if((a+b)%2==(c+d)%2):
        print("YES")
    else:
        print("NO")
