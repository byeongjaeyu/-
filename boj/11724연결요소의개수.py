from collections import deque

n,m = map(int, input().split())
ve_lst = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    ve_lst[a].append(b)
    ve_lst[b].append(a)

def solution():
    while q:
        p = q.popleft()
        for place in ve_lst[p]:
            if visited[place] == 0:
                q.append(place)
                visited[place] = visited[p]

for i in range(1,n+1):
    q = deque()
    if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        solution()

print(len(set(visited))-1)
