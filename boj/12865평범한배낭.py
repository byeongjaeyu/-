n,k = map(int, input().split())
wv_lst = [list(map(int, input().split())) for _ in range(n)]
wv_lst.sort(key=lambda x:x[0])
dp = [[0]*(k+1) for _ in range(n+1)]
for sel in range(n+1):
    dp[sel][0] = 0
for w in range(k+1):
    dp[0][w] = 0

for sel in range(1,n+1):
    for w in range(1,k+1):
        if w>=wv_lst[sel-1][0]:
            dp[sel][w] = max(dp[sel-1][w-wv_lst[sel-1][0]] + wv_lst[sel-1][1],dp[sel-1][w])
        else:
            dp[sel][w] = dp[sel-1][w]

print(dp[-1][-1])