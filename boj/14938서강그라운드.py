n,m,r = map(int, input().split())
items = [0]+list(map(int, input().split()))
uv_lst = [dict() for _ in range(n+1)]
for i in range(r):
    u,v,w = map(int, input().split())
    if uv_lst[u].get(v) == None:
        uv_lst[u][v] = w
    else:
        uv_lst[u][v] = min(uv_lst[u][v],w)

    if uv_lst[v].get(u) == None:
        uv_lst[v][u] = w
    else:
        uv_lst[v][u] = min(uv_lst[v][u],w)

val = [[0xffffffff]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            val[i][j] = 0
        elif uv_lst[i].get(j):
            if uv_lst[i][j] <= m:
                val[i][j] = uv_lst[i][j]


for mid in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if (val[s][mid]+val[mid][e] < val[s][e]):
                val[s][e] = val[s][mid]+val[mid][e]

ans = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        if val[i][j] <= m:
            temp += items[j]
    ans = max(ans,temp)

print(ans)