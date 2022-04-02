n = int(input())
ve_lst = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j]:
            ve_lst[i].append(j)

ans_lst = [[0]*n for _ in range(n)]

from collections import deque
def bfs():
    while q:
        p = q.popleft()
        for a in ve_lst[p]:
            if not visited[a]:
                visited[a] = 1
                q.append(a)


for i in range(n):
    visited = [0]*n
    q = deque()
    q.append(i)
    visited[i] = 0
    bfs()
    for j in range(n):
        if visited[j]:
            ans_lst[i][j] = 1

for i in range(n):
    print(*ans_lst[i])


        
