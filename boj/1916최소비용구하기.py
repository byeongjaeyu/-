from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
uv_lst = [dict() for _ in range(n+1)]
for i in range(m):
    u,v,w = map(int, input().split())
    if uv_lst[u].get(v) == None:
        uv_lst[u][v] = w
    else:
        uv_lst[u][v] = min(uv_lst[u][v],w)
s,e = map(int, input().split())
value = [0xffffffff]*(n+1)
value[s] = 0

from heapq import heappop, heappush

q = []
heappush(q,[0,s])
while q:
    val,node = heappop(q)
    for des in uv_lst[node]:
        if value[des] > val+uv_lst[node][des]:
            value[des] = val+uv_lst[node][des]
            heappush(q,[value[des],des])

print(value[e])
