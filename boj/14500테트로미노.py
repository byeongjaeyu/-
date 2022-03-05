n,m = map(int, input().split())
num_lst = [list(map(int, input().split())) for _ in range(n)]

def DFS(i1:int,i2:int):
    global ans, cnt, s1
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

dr = [-1,1,0,0]
dc = [0,0,-1,1]

idx_lst = [
[0,1,2],
[0,1,3],
[1,2,3],
[0,2,3],
]

ans = 0
for i1 in range(n):
    for i2 in range(m):
        cnt = 1
        visited = [[0]*m for _ in range(n)]
        visited[i1][i2] = 1
        s1 = num_lst[i1][i2]
        DFS(i1,i2)

        for lst in idx_lst:
            s2 = num_lst[i1][i2]
            for i in lst:
                r = i1+dr[i];  c = i2+dc[i]
                if(0<=r<n and 0<=c<m):
                    s2 += num_lst[r][c]

            ans = max(s2,ans)

print(ans)