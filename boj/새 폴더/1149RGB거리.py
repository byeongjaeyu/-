n = int(input())
rgb_cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = rgb_cost[0]
dp[1][0] = min(dp[0][1],dp[0][2])+rgb_cost[1][0]
dp[1][1] = min(dp[0][0],dp[0][2])+rgb_cost[1][1]
dp[1][2] = min(dp[0][0],dp[0][1])+rgb_cost[1][2]

for i in range(2,n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+rgb_cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+rgb_cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+rgb_cost[i][2]

print(min(dp[n-1]))
