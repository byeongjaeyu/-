n,m = map(int, input().split())
from collections import deque

lie_lst = list(map(int, input().split()))
q = deque()
visited = [0]*(n+1)
if lie_lst[0] == 0:
    print(m)
else:
    for i in range(1,len(lie_lst)):
        visited[lie_lst[i]] = 1
        q.append(lie_lst[i])

    party_lst = [list(map(int ,input().split())) for _ in range(m)]

    while q:
        p = q.popleft()
        for party in party_lst:
            if p in party[1:]:
                for ppl in party[1:]:
                    if not visited[ppl]:
                        q.append(ppl)
                        visited[ppl] = 1
    ans = 0
    for party in party_lst:
        for ppl in party[1:]:
            if visited[ppl] == 1:
                break
        else:
            ans += 1

    print(ans)
