from sys import stdin
input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
color = [[0]*n for _ in range(n)]
avails = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            avails.append([i,j])
for avail in avails:
    i,j = avail[0],avail[1]
    if i%2 == 0:
        if j%2 == 1:
            color[i][j] = 'B'
        else:
            color[i][j] = 'W'
    else:
        if j%2 == 1:
            color[i][j] = 'W'
        else:
            color[i][j] = 'B'
plus_visited = [0]*(2*n)
minus_visited = [0]*(2*n)
ans = 0
def solution(cnt:int,s_idx:int,col:str):
    global ans
    if s_idx >= len(avails):
        return
    for idx in range(s_idx,len(avails)):
        avail = avails[idx]
        if color[avail[0]][avail[1]] == col:
            p = avail[0]+avail[1]
            m = avail[0]-avail[1]+n-1
            if plus_visited[p] == 1 or minus_visited[m] == 1:
                continue
            plus_visited[p] = 1
            minus_visited[m] = 1
            ans = max(ans,cnt+1)
            solution(cnt+1,idx+1,col)
            plus_visited[p] = 0
            minus_visited[m] = 0

for idx in range(len(avails)):
    if color[avails[idx][0]][avails[idx][1]] == 'B':
        solution(0,0,'B')
b_max = ans

plus_visited = [0]*(2*n)
minus_visited = [0]*(2*n)
ans = 0
for idx in range(len(avails)):
    if color[avails[idx][0]][avails[idx][1]] == 'W':
        solution(0,0,'W')
w_max = ans
print(b_max+w_max)