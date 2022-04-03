a = input()
b = input()

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i1 in range(1,len(a)+1):
    for i2 in range(1,len(b)+1):
        if a[i1-1] == b[i2-1]:
            dp[i1][i2] = dp[i1-1][i2-1]+1
        else:
            dp[i1][i2] = max(dp[i1-1][i2],dp[i1][i2-1])

for i in range(len(a)+1):
    print(*dp[i])
