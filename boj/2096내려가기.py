from sys import stdin
input = stdin.readline
n = int(input())
nums = list(map(int , input().split()))

dp = [[0,0xffffffff]for _ in range(3)]
dp = [[nums[0],nums[0]],[nums[1],nums[1]],[nums[2],nums[2]]]
for i in range(1,n):
    nums = list(map(int, input().split()))
    save = dp[:][:]
    dp[0] = [max(save[0][0],save[1][0])+nums[0],min(save[0][1],save[1][1])+nums[0]]
    dp[1] = [max(save[0][0],save[1][0],save[2][0])+nums[1],min(save[0][1],save[1][1],save[2][1])+nums[1]]
    dp[2] = [max(save[1][0],save[2][0])+nums[2],min(save[1][1],save[2][1])+nums[2]]

maxv = 0
minv = 0xffffffff
for i in range(3):
    v1,v2 = dp[i]
    maxv = max(maxv,v1)
    minv = min(minv,v2)

print(maxv,minv)
