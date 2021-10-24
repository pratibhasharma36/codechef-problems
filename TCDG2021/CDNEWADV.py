#https://www.codechef.com/TCDG2021/problems/CDNEWADV
testcases = int(input())
for test in range (0, testcases):
    m, n = map(int, input().split())
    seta = set(map(str, input().split()))
    setb = set(map(str, input().split()))
    setb = setb.intersection(seta)
    print(len(setb))
