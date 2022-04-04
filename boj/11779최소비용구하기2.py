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

val = [0xffffffff]*(n+1)
s,e = map(int, input().split())
val[s] = 0

from heapq import heappop, heappush
ans = 0xffffffff
ans_len = 0
ans_way = ""
q = []
heappush(q,[0,s,[s]])
while q:
    value,pos,way = heappop(q)
    if pos == e:
        if value<ans:
            ans = value
            ans_len = len(way)
            ans_way = " ".join(map(str,way))
        # print(' '.join(map(str,way)))
    for des in uv_lst[pos]:
        if val[des] > value + uv_lst[pos][des]:
            val[des] = value + uv_lst[pos][des]
            heappush(q,[val[des],des,way+[des]])

print(ans)
print(ans_len)
print(ans_way)