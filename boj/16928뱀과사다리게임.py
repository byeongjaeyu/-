n,m = map(int, input().split())
ladders = dict()
for i in range(n):
    a,b = map(int, input().split())
    ladders[a] = b
snakes = dict()
for i in range(m):
    a,b = map(int, input().split())
    snakes[a] = b

visited = [0]*101

from collections import deque

def bfs():
    while q:
        p = q.popleft()
        if p == 100:
            return visited[100]
        for i in range(1,7):
            p2 = p+i
            if 1<=p2<=100 and not visited[p2]:
                visited[p2] = visited[p] + 1
                a = ladders.get(p2)
                b = snakes.get(p2)
                if a:
                    visited[a] = visited[p2]
                    q.append(a)
                elif b:
                    visited[b] = visited[p2]
                    q.append(b)
                else:
                    q.append(p2)

q = deque()
q.append(1)
visited[1] = 1
print(bfs()-1)