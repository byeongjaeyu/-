n,m = map(int, input().split())
fe_lst = [[] for _ in range(n+1)]
ef_lst = [[] for _ in range(n+1)]

for i in range(m):
    f,e = map(int, input().split())
    fe_lst[f].append(e)
    ef_lst[e].append(f)

fe_cnt_lst = [len(fe_lst[i]) for i in range(n+1)]
print(fe_cnt_lst)

from heapq import heappop,heappush
q = []
for i in range(1,n+1):
    if fe_cnt_lst[i] == 0:
        heappush(q,[i,0,i])

ans = []
while q:
    org,lev,p = heappop(q)
    flag = True
    for num in ef_lst[p]:
        if fe_cnt_lst[num] != 0:
            flag = False
            fe_cnt_lst[num] -= 1
            if fe_cnt_lst[num] == 0:
                heappush(q,[org,lev,num])
    if flag:
        ans.append(p)
    else:
        heappush(q,[org,lev+1,p])

print(' '.join(map(str,ans)))
        