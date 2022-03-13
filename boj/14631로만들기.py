n = int(input())
dp = [0] * (n+1)
dp[1] = 0
for i in range(2,n+1):
    if not i%3 and not i%2:
        dp[i] = min(dp[i-1],dp[i//3],dp[i//2])+1
    elif not i%3 and i%2:
        dp[i] = min(dp[i-1],dp[i//3])+1
    elif not i%2 and i%2:
        dp[i] = min(dp[i-1],dp[i//2])+1
    else:
        dp[i] = dp[i-1]+1

print(dp[n])