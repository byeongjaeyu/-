from sys import stdin
input = stdin.readline
n = int(input())

dp = [[None]*n for _ in range(n)]

for i in range(n):
    tri_lst = list(map(int, input().split()))
    if i==0:
        dp[i][0] = tri_lst[0]
    else:
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + tri_lst[j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + tri_lst[j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + tri_lst[j]

print(max(dp[-1]))
            
