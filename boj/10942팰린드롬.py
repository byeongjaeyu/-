from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for i in range(n):
    for j in range(n):
        if i>j:
            if i==j+1:
                if(nums[i]==nums[j]):
                    dp[j][i] = 1
            else:
                if(dp[j+1][i-1]==1 and nums[i]==nums[j]):
                    dp[j][i] = 1

for _ in range(m):
    s,e = map(int, input().split())
    print('{}\n'.format(dp[s-1][e-1]))