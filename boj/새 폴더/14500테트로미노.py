from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
num_lst = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
for i in range(n):
    for j in range(m):
        max_val = max(max_val,num_lst[i][j])

def DFS(i1:int,i2:int):
    global ans, cnt, s1
    if s1+(4-cnt)*max_val <= ans:
        return 
    if cnt >= 4:
        ans = max(ans,s1)
        return
    for i in range(4):
        r = i1+dr[i];  c = i2+dc[i]
        if (0<=r<n and 0<=c<m and visited[r][c] == 0):
            visited[r][c] = 1
            s1 += num_lst[r][c]
            cnt += 1
            DFS(r,c)
            visited[r][c] = 0
            s1 -= num_lst[r][c]
            cnt -= 1

def BFS(i1:int,i2:int):
    global ans
    near = []
    for i in range(4):
        r = i1+dr[i]; c = i2+dc[i]
        if (0<=r<n and 0<=c<m):
            near.append(num_lst[r][c])
    
    if len(near) >= 3:
        near.sort(reverse=True)
        max_bfs = num_lst[i1][i2] + sum(near[0:3])
        ans = max(ans,max_bfs)


dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]

ans = 0
for i1 in range(n):
    for i2 in range(m):
        cnt = 1
        visited[i1][i2] = 1
        s1 = num_lst[i1][i2]
        DFS(i1,i2)
        visited[i1][i2] = 0
        BFS(i1,i2)

print(ans)