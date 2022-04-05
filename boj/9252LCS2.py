a = list(input())
b = list(input())

dp = [[[0,[]] for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i1 in range(1,len(a)+1):
    if i1>=2:
        dp[i1-2].clear()
    for i2 in range(1,len(b)+1):
        if a[i1-1] == b[i2-1]:
            dp[i1][i2] = [dp[i1-1][i2-1][0]+1,dp[i1-1][i2-1][1]+[a[i1-1]]]
        else:
            if dp[i1-1][i2][0] >= dp[i1][i2-1][0]:
                dp[i1][i2] = dp[i1-1][i2]
            else:
                dp[i1][i2] = dp[i1][i2-1]

print(dp[-1][-1][0])
print(''.join(map(str,dp[-1][-1][1])))
