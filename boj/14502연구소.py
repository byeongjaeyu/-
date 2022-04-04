n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

defaultwall = 0

for i in range(n):
    for j in range(m):
        if lab[i][j] == 1:
            defaultwall += 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

from collections import deque

ans = 0

def virus():
    save_lab = lab[:][:]
    visited = [[0]*m for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if save_lab[i][j] == 2 and not visited[i][j]:
                q.append([i,j])
                visited[i][j] = 1
                cnt += 1
                while q:
                    idx1,idx2 = q.popleft()
                    for dir in range(4):
                        r = idx1 + dr[dir]
                        c = idx2 + dc[dir]
                        if 0<=r<n and 0<=c<m and save_lab[r][c] == 0 and not visited[r][c]:
                            q.append([r,c])
                            visited[r][c] = 1
                            cnt += 1

    return (n*m)-cnt-3-defaultwall
    


def wall(cnt:int):
    global ans
    if cnt == 4:
        val = virus()
        ans = max(ans,val)
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0
wall(1)

print(ans)