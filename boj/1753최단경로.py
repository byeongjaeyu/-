from sys import stdin
input = stdin.readline


v,e = map(int, input().split())
k = int(input())
value = [200001]*(v+1)
uv_lst = [dict() for _ in range(v+1)]
for i in range(e):
    u,v,w = map(int, input().split())
    if uv_lst[u].get(v) == None:
        uv_lst[u][v] = w
    else:
        uv_lst[u][v] = min(uv_lst[u][v],w)


from collections import deque
from heapq import heappop, heappush
q = []
heappush(q,[0,k])
value[k] = 0
while q:
    p = heappop(q)
    for key in uv_lst[p[1]]:
        if value[key] > p[0] + uv_lst[p[1]][key]:
            value[key] = p[0] + uv_lst[p[1]][key]
            heappush(q,[value[key],key])

for i in range(1,len(value)):
    if value[i] >= 200001:
        print('INF')
    else:
        print(value[i])