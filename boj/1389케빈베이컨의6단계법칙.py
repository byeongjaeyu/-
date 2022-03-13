n,m = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
from collections import deque

def bfs():
    while q:
        p = q.popleft()
        lev = visited[p]
        for ppl in lst[p]:
            if not visited[ppl]:
                q.append(ppl)
                visited[ppl] = lev + 1
    return
    
ans = [n**2,0]
for i in range(1,n+1):
    visited = [0]*(n+1)
    q = deque()
    q.append(i)
    visited[i] = 1
    bfs()
    lev = sum(visited)
    if lev<ans[0]:
        ans = [lev,i]
    elif lev == ans[0]:
        ans = [lev,min(i,ans[1])]

print(ans[1])