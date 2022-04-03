n,k = map(int, input().split())
from heapq import heappop, heappush
val = [0xffffffff]*(100001)
val[n] = 0
def go():
    while q:
        v,p = heappop(q)
        if p == k:
            return v
        if 0<=p+1<=100000 and v+1<val[p+1]:
            val[p+1] = v+1
            heappush(q,[v+1,p+1])
        if 0<=p-1<=100000 and v+1<val[p-1]:
            val[p-1] = v+1
            heappush(q,[v+1,p-1])
        if 0<=2*p<=100000 and v<val[2*p]:
            val[2*p] = v
            heappush(q,[v,2*p])
q = []
heappush(q,[0,n])
print(go())