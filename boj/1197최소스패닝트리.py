v,e = map(int, input().split())
# uv_lst = [[] for _ in range(v+1)]
# for i in range(e):
#     u,v,w = map(int, input().split())
#     uv_lst[u].append([v,w])
#     uv_lst[v].append([u,w])
parent = [i for i in range(v+1)]

lines = [list(map(int, input().split())) for _ in range(e)]
lines.sort(key=lambda x:x[2])


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    roota = find(a)
    rootb = find(b)
    if roota < rootb:
        parent[rootb] = roota
    else:
        parent[roota] = rootb

ans = 0
for line in lines:
    a,b,cost = line
    if find(a) != find(b):
        union(a,b)
        ans += cost
print(ans)
