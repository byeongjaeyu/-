from collections import deque
n,m = map(int, input().split())
map_lst = [[] for _ in range(n)]
for i in range(n):
    map_lst[i] = list(map(str,input()))

ans = n*m

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]

def bfs():
    while q:
        x,y = q.popleft()
        if x==n-1 and y==m-1:
            return
        for i in range(4):
            r = x+dr[i]
            c = y+dc[i]
            if 0<=r<n and 0<=c<m and map_lst[r][c]=='1' and not visited[r][c]:
                visited[r][c] = visited[x][y] + 1
                q.append([r,c])

visited[0][0] = 1
q = deque()
q.append([0,0])
bfs()

print(visited[n-1][m-1])