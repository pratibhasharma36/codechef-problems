#https://www.codechef.com/TCDG2021/problems/CDTRESUM
n = int(input())
left_node = [0 for i in range (0, 100001)]
right_node = [0 for i in range (0, 100001)]
val = [0 for i in range (0, 100001)]
sum_val = [0 for i in range (0, 100001)]
ls = [0]
def dfs(node):
    sum_val[node] = ls.pop() + val[node]
    ls.append(sum_val[node])
    if(left_node[node]!=0):
        dfs(left_node[node])
    if(right_node[node]!=0):
        dfs(right_node[node])
for i in range (1, n+1):
    left_node[i], right_node[i], val[i] = map(int, input().split())
dfs(1)
queries = int(input())
for i in range (0, queries):
    a, b = map(int, input().split())
    print(sum_val[b]-sum_val[a]-val[b])
    
