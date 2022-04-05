n = int(input())
dp = [[0,[]] for _ in range(n+1)]
dp[1] = [0,[1]]
for i in range(2,n+1):

    dp[i] = [dp[i-1][0]+1,dp[i-1][1]+[i]]

    if not i%2:
        if dp[i][0]>dp[i//2][0]+1:
            dp[i] = [dp[i//2][0]+1,dp[i//2][1]+[i]]

    if not i%3:
        if dp[i][0]>dp[i//3][0]+1:
            dp[i] = [dp[i//3][0]+1,dp[i//3][1]+[i]]

print(dp[n][0])
print(' '.join(map(str,dp[n][1][::-1])))