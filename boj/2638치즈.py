n,m = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
from collections import deque
flag = True
cnt = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
while flag:
    visited = [[0]*m for _ in range(n)]
    for_flag = True
    for i in range(n):
        for j in range(m):
            if map_lst[i][j] == 0 and not visited[i][j]:
                q = deque()
                q.append([i,j])
                while q:
                    idx1,idx2 = q.popleft()
                    for i in range(4):
                        r = idx1 + dr[i]
                        c = idx2 + dc[i]
                        if 0<=r<n and 0<=c<m:
                            if map_lst[r][c] == 0 and visited[r][c] == 0:
                                visited[r][c] = 1
                                q.append([r,c])
                            elif map_lst[r][c] == 1:
                                visited[r][c] -= 1
                for_flag = False
                break
        if not for_flag:
            break
                
    is_melt = False
    for i in range(n):
        for j in range(m):
            if visited[i][j] <= -2:
                map_lst[i][j] = 0
                is_melt = True

    if not is_melt:
        flag = False

    if flag:
        cnt += 1

print(cnt)
                        
