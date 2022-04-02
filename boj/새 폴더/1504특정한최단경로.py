n,e = map(int, input().split())
uv_lst = [[] for _ in range(n+1)]
for i in range(e):
    v1,v2,c = map(int, input().split())
    uv_lst[v1].append([v2,c])
    uv_lst[v2].append([v1,c])

musts = list(map(int, input().split()))



def dijkstra(s,e):
    q = deque()
    q.append(s)
    value = [800001]*(n+1)
    value[s] = 0
    while q:
        p = q.popleft()
        for line in uv_lst[p]:
            if value[line[0]] > value[p] + line[1]:
                value[line[0]] = value[p] + line[1]
                q.append(line[0])
    return value[e]
    
from collections import deque


path1 = dijkstra(1,musts[0]) + dijkstra(musts[0],musts[1]) + dijkstra(musts[1],n)
path2 = dijkstra(1,musts[1]) + dijkstra(musts[1],musts[0]) + dijkstra(musts[0],n)

if path1 >= 800001 and path2>=800001:
    print(-1)
else:
    print(min(path1,path2))