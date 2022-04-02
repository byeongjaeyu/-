n,m,x = map(int, input().split())
road_lst = [[] for _ in range(n+1)]
for i in range(m):
    s,e,v = map(int, input().split())
    road_lst[s].append([e,v])

value = [100000]*(n+1)
value[x] = 0
from collections import deque

q = deque()
q.append(x)

while q:
    p = q.popleft()
    for road in road_lst[p]:
        if value[p]+road[1] < value[road[0]]:
            q.append(road[0])
            value[road[0]] = value[p] + road[1]


gotox = [0]*(n+1)
for i in range(1,n+1):
    if i==x:continue
    else:
        q = deque()
        q.append(i)
        go = [100000]*(n+1)
        go[i] = 0
        while q:
            p = q.popleft()
            for road in road_lst[p]:
                if go[p]+road[1] < go[road[0]]:
                    q.append(road[0])
                    go[road[0]] = go[p] + road[1]
        gotox[i] = go[x]


ans = 0

for i in range(1,n+1):
    if i==x:continue
    else:
        ans = max(ans,gotox[i]+value[i])

print(ans)