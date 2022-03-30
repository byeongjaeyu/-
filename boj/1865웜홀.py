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

    for i in range(1,n+1):
        q = []
        val = [0xffffffff] * (n+1)
        heappush(q,[0,i])
        val[i] = 0
        while q:
            if val[i] < 0:
                break
            value,point = heappop(q)
            for key in uv_lst[point]:
                if val[key] > uv_lst[point][key] + value:
                    val[key] = uv_lst[point][key] + value
                    heappush(q,[val[key],key])
        if val[i]<0:
            print('YES')
            break
    else:
        print('NO')
    

