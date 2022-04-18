n,m = map(int, input().split())
bites = list(map(int, input().split()))
costs = list(map(int, input().split()))
b_c = [[] for _ in range(n)]
for i in range(n):
    b_c[i] = [bites[i],costs[i]]
b_c.sort(key=lambda x:x[0])
dp = [[0]*(m+1) for _ in range(n+1)]
ans = 0xffffffff
for app_i in range(1,n+1):
    for byte in range(1,m+1):
        if byte >= b_c[app_i-1][0]:
            dp[app_i][byte] = max(dp[app_i][byte-1],b_c[app_i-1][0]+dp[app_i-1][byte-b_c[app_i-1][1]])
        else:
            dp[app_i][byte] = dp[app_i-1][byte]
        if dp[app_i][byte] >= m:
            ans = min(ans,byte)

print(ans)

