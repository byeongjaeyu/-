n,k = map(int, input().split())
from collections import deque
q = deque()
q.append(n)
visited = [0]*100001
ans = 0xffffffff
cnt = 0
while q:
    pos = q.popleft()
    val = visited[pos]

    if visited[k] and val+(pos-k) > visited[k]:
        continue
    
    if pos == k:
        if val<ans:
            ans = val
            cnt = 1
        elif val==ans:
            cnt += 1
        continue

    if pos+1<=100000 and not visited[pos+1]:
        visited[pos+1] = val+1
        q.append(pos+1)
    elif pos+1<=100000 and val+1==visited[pos+1]:
        q.append(pos+1)

    if pos-1>=0 and not visited[pos-1]:
        visited[pos-1] = val+1
        q.append(pos-1)
    elif pos-1>=0 and val+1==visited[pos-1]:
        q.append(pos-1)

    if pos*2<=100000 and not visited[pos*2]:
        visited[pos*2] = val+1
        q.append(pos*2)
    elif pos*2<=100000 and val+1==visited[pos*2]:
        q.append(pos*2)

print(ans, cnt)