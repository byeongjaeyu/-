n = int(input())
dp = [0]*(50001)
dp[0] = 0xffffff
dp[1] = 1
for i in range(2,50001):
    dp_min = 50000
    minus_sq = 1
    while True:
        idx = i-(minus_sq**2)
        if idx == 0:
            dp_min = 0
            break
        elif idx < 0:
            break
        else:
            dp_min = min(dp[idx],dp_min)
            minus_sq += 1
    dp[i] = dp_min + 1

print(dp[n])