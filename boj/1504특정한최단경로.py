n,e = map(int, input().split())
uv_lst = [[] for _ in range(n+1)]
for i in range(e):
    v1,v2,c = map(int, input().split())
    uv_lst[v1].append([v2,c])
    uv_lst[v2].append([v1,c])

musts = list(map(int, input().split()))
for i in range(len(musts)):
    num = musts[i]
    musts[i] = [num,0]


value = [800000]*(n+1)
value[1] = 0

from collections import deque
q = deque()
q.append([1,0,0])

while q:
    p = q.popleft()

    for must in musts:
        if p == must[0]:
            must[1] = 1
            break
    
    for line in uv_lst[p]:
        