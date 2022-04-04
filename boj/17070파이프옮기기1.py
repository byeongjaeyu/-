n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0]for __ in range(n)] for _ in range(n)] #가로,세로,대각
dp[0][0] = [0,0,0]
dp[0][1] = [1,0,0]

for i in range(n):
    for j in range(n):
        if i==0 and (j==0 or j==1):
            continue
        elif home[i][j] == 1:
            continue
        else:
            if(j-1>=0):
                dp[i][j][0] = dp[i][j-1][2]+dp[i][j-1][0]
            if(i-1>=0 and j-1>=0 and home[i][j-1]!=1 and home[i-1][j]!=1):
                dp[i][j][2] = sum(dp[i-1][j-1])
            if(i-1>=0):
                dp[i][j][1] = dp[i-1][j][1]+dp[i-1][j][2]

print(sum(dp[-1][-1]))
