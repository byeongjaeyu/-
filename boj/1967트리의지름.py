from sys import stdin
input = stdin.readline
n = int(input())
uv_lst = [[] for _ in range(n+1)]
for i in range(n-1):
    u,v,w = map(int, input().split())
    uv_lst[u].append([v,w])
    uv_lst[v].append([u,w])

ans = [0,0]
def dfs(n:int,d:int):
    global ans
    if d>ans[1]:
        ans = [n,d]
    for node,weight in uv_lst[n]:
        if not visited[node]:
            visited[node] = 1
            dfs(node,d+weight)
            visited[node] = 0
visited = [0]*(n+1)
visited[1] = 1
dfs(1,0)
visited[1] = 0

s = ans[0]
ans = [0,0]
visited[s] = 1
dfs(s,0)

print(ans[1])