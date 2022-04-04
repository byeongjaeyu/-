n,b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
def solution(sqr:int):
    if sqr == 1:
        return matrix
    else:
        if sqr%2 == 0:
            temp = solution(sqr//2)
            new_mat = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        new_mat[i][j] += temp[i][k]*temp[k][j]
                    new_mat[i][j] %= 1000
            return new_mat
        else:
            temp = solution(sqr-1)
            new_mat = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        new_mat[i][j] += matrix[i][k]*temp[k][j]
                    new_mat[i][j] %= 1000
            return new_mat

ans = solution(b)

for i in range(n):
    for j in range(n):
        ans[i][j] %= 1000

for i in range(n):
    print(*ans[i])
