from sys import stdin
input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
plus_visited = [0]*(2*n)
minus_visited = [0]*(2*n)
ans = 0
def solution(cnt:int):
    global ans
    ans = max(ans,cnt)
    for i in range(n):
        for j in range(n):
            p = i+j
            m = i-j+n-1
            if plus_visited[p] == 1 or minus_visited[m] == 1:
                continue
            if board[i][j] == 1:
                board[i][j] = 0
                plus_visited[p] = 1
                minus_visited[m] = 1
                solution(cnt+1)
                board[i][j] = 1
                plus_visited[p] = 0
                minus_visited[m] = 0

solution(0)
print(ans)