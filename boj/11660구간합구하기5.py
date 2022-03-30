n,m = map(int ,input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = nums[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i-1]+nums[0][i]
    dp[i][0] = dp[i-1][0]+nums[i][0]

for i1 in range(1,n):
    for i2 in range(1,n):
        dp[i1][i2] = dp[i1-1][i2] + dp[i1][i2-1] - dp[i1-1][i2-1] + nums[i1][i2]

for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    x1-=1;y1-=1;x2-=1;y2-=1
    ans = dp[x2][y2]
    if x1>=1:
        ans -= dp[x1-1][y2]
    if y1>=1:
        ans -= dp[x2][y1-1]
    if x1>=1 and y1>=1:
        ans += dp[x1-1][y1-1]
    
    print(ans)
