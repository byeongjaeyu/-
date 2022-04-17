from sys import stdin
input = stdin.readline
n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]
dp_0 = [[0]*3 for _ in range(n)]
dp_1 = [[0]*3 for _ in range(n)]
dp_2 = [[0]*3 for _ in range(n)]
dp_0[0][0] = rgbs[0][0]
dp_1[0][1] = rgbs[0][1]
dp_2[0][2] = rgbs[0][2]

dp_0[1][1] = dp_0[0][0] + rgbs[1][1]
dp_0[1][2] = dp_0[0][0] + rgbs[1][2]

dp_1[1][0] = dp_1[0][1] + rgbs[1][0]
dp_1[1][2] = dp_1[0][1] + rgbs[1][2]

dp_2[1][0] = dp_2[0][2] + rgbs[1][0]
dp_2[1][1] = dp_2[0][2] + rgbs[1][1]

if n>=3:
    dp_0[2][0] = min(dp_0[1][1],dp_0[1][2]) + rgbs[2][0]
    dp_0[2][1] = dp_0[1][2] + rgbs[2][1]
    dp_0[2][2] = dp_0[1][1] + rgbs[2][2]

    dp_1[2][0] = dp_1[1][2] + rgbs[2][0]
    dp_1[2][1] = min(dp_1[1][0],dp_1[1][2]) + rgbs[2][1]
    dp_1[2][2] = dp_1[1][0] + rgbs[2][2]

    dp_2[2][0] = dp_2[1][1] + rgbs[2][0]
    dp_2[2][1] = dp_2[1][0] + rgbs[2][1]
    dp_2[2][2] = min(dp_2[1][0],dp_2[1][1]) + rgbs[2][2]

if n>=4:
    for i in range(3,n-1):
        dp_0[i][0] = min(dp_0[i-1][1],dp_0[i-1][2]) + rgbs[i][0]
        dp_0[i][1] = min(dp_0[i-1][0],dp_0[i-1][2]) + rgbs[i][1]
        dp_0[i][2] = min(dp_0[i-1][0],dp_0[i-1][1]) + rgbs[i][2]

        dp_1[i][0] = min(dp_1[i-1][1],dp_1[i-1][2]) + rgbs[i][0]
        dp_1[i][1] = min(dp_1[i-1][0],dp_1[i-1][2]) + rgbs[i][1]
        dp_1[i][2] = min(dp_1[i-1][0],dp_1[i-1][1]) + rgbs[i][2]

        dp_2[i][0] = min(dp_2[i-1][1],dp_2[i-1][2]) + rgbs[i][0]
        dp_2[i][1] = min(dp_2[i-1][0],dp_2[i-1][2]) + rgbs[i][1]
        dp_2[i][2] = min(dp_2[i-1][0],dp_2[i-1][1]) + rgbs[i][2]

    dp_0[n-1][1] = min(dp_0[n-2][0],dp_0[n-2][2]) + rgbs[n-1][1]
    dp_0[n-1][2] = min(dp_0[n-2][0],dp_0[n-2][1]) + rgbs[n-1][2]
    ans = min(dp_0[n-1][1],dp_0[n-1][2])
    dp_1[n-1][0] = min(dp_1[n-2][1],dp_1[n-2][2]) + rgbs[n-1][0]
    dp_1[n-1][2] = min(dp_1[n-2][0],dp_1[n-2][1]) + rgbs[n-1][2]
    ans = min(ans,dp_1[n-1][0],dp_1[n-1][2])
    dp_2[n-1][0] = min(dp_2[n-2][1],dp_2[n-2][2]) + rgbs[n-1][0]
    dp_2[n-1][1] = min(dp_2[n-2][0],dp_2[n-2][2]) + rgbs[n-1][1]
    ans = min(ans,dp_2[n-1][0],dp_2[n-1][1])

    print(ans)
else:
    print(min(dp_0[-1][1],dp_0[-1][2],dp_1[-1][0],dp_1[-1][2],dp_2[-1][0],dp_2[-1][1]))
