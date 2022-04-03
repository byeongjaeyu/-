from sys import stdin
input = stdin.readline
from heapq import heappop, heappush
for test in range(int(input())):
    n,m,wo = map(int, input().split())

    uv_lst = [dict() for _ in range(n+1)]
    for i in range(m):
        u,v,w = map(int, input().split())
        if uv_lst[u].get(v) == None:
            uv_lst[u][v] = w
        else:
            uv_lst[u][v] = min(uv_lst[u][v],w)

        if uv_lst[v].get(u) == None:
            uv_lst[v][u] = w
        else:
            uv_lst[v][u] = min(uv_lst[v][u],w)
    
    for i in range(wo):
        u,v,w = map(int, input().split())
        w = (-1)*w
        if uv_lst[u].get(v) == None:
            uv_lst[u][v] = w
        else:
            uv_lst[u][v] = min(uv_lst[u][v],w)
    

    val = [0xffffffff] * (n+1)
    is_cycle = False
    for c in range(n):
        for u in range(1,n+1):
            for v in uv_lst[u]:
                if val[v] > val[u] + uv_lst[u][v]:
                    val[v] = val[u] + uv_lst[u][v]
                    if c == n-1:
                        is_cycle = True
                        break
            if is_cycle: break
        if is_cycle: break
    
    print('YES') if is_cycle else print('NO')