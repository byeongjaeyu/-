from sys import stdin
input = stdin.readline
for test in range(int(input())):
    n = int(input())
    dp = [[0]*n for _ in range(2)]
    stickers = [list(map(int, input().split())) for _ in range(2)]
    for i2 in range(n):
        for i1 in range(2):
            if i2-2>=0:
                dp[i1][i2] = max(dp[(i1+1)%2][i2-1],dp[(i1+1)%2][i2-2])+stickers[i1][i2]
            elif i2-1>=0:
                dp[i1][i2] = dp[(i1+1)%2][i2-1]+stickers[i1][i2]
            else:
                dp[i1][i2] = stickers[i1][i2]
    print(max(dp[0][-1],dp[1][-1]))