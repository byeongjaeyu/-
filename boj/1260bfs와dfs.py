def dfs(n:int):
    ans_1.append(n)
    visited_1[n] = 1
    for k in lst[n]:
        if not visited_1[k]:
            dfs(k)

def bfs():
    while q:
        p = q.popleft()
        for k in lst[p]:
            if not visited_2[k]:
                visited_2[k] = 1
                ans_2.append(k)
                q.append(k)

n,m,v = map(int, input().split())
lst = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int ,input().split())
    lst[a].append(b)
    lst[b].append(a)
    
for l in lst:
    l.sort()
ans_1 = []
visited_1 = [0]*(n+1)
dfs(v)
print(*ans_1)
from collections import deque
visited_2 = [0]*(n+1)
q = deque()
visited_2[v] = 1
q.append(v)
ans_2 = [v]
bfs()
print(*ans_2)