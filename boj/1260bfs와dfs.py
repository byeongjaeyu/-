def dfs(n:int):
    for i in range()

n,m,v = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int ,input().split())
    lst[a].append(b)
    lst[b].append(a)

dfs(v)
bfs()