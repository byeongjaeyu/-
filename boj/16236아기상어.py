n = int(input())
map_lst = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,-1,0,1]
from collections import deque
def bfs():
    while q:
        i,j = q.popleft()
        if map_lst[i][j] and map_lst[i][j] < cur_scale[0]:
            map_lst[i][j] = 0
            return [[i,j],visited[i][j]]
        for d in range(4):
            r = i+dr[d]; c = j + dc[d]
            if 0<=r<n and 0<=c<n and not visited[r][c] and map_lst[r][c] <= cur_scale[0]:
                visited[r][c] = visited[i][j] + 1
                q.append([r,c])
        
for i in range(n):
    for j in range(n):
        if map_lst[i][j] == 9:
            map_lst[i][j] = 0
            cur_scale = [2,0]
            time = 0
            visited = [[0]*n for _ in range(n)]
            visited[i][j] = 1
            q = deque()
            q.append([i,j])
            while True:
                val = bfs()
                if val:
                    time += val[1]
                    visited = [[0]*n for _ in range(n)]
                    visited[val[0][0]][val[0][1]] = 1
                    cur_scale[1] += 1
                    if cur_scale[1] == cur_scale[0]:
                        cur_scale = [cur_scale[0]+1,0]
                    q = deque()
                    q.append([val[0][0],val[0][1]])
                else:
                    break

print(time)


