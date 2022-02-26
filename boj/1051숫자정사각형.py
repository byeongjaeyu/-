n,m = map(int, input().split())
square_lst = [list(map(int,input())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        num = square_lst[i][j]
        max_len = 1
        while True:
            if (i+max_len<n) and (j+max_len<m):
                if num == square_lst[i][j+max_len] == square_lst[i+max_len][j] == square_lst[i+max_len][j+max_len]:
                    ans = max(ans,max_len)
                    max_len += 1
                else:
                    max_len += 1
            else:
                break

print(1) if ans == 0 else print((ans+1)**2)