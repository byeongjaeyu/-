def solution():
    global ans
    while q:
        p = q.popleft()
        for com in ve_lst[p]:
            if visited[com] == 0:
                visited[com] = 1
                ans += 1
                q.append(com)


from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ve_lst = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int ,sys.stdin.readline().split())
    ve_lst[a].append(b)
    ve_lst[b].append(a)

visited = [0] * (n+1)
visited[1] = 1
q = deque()
q.append(1)
ans = 0
solution()
print(ans)
