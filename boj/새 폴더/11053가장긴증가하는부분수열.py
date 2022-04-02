n = int(input())
nums = list(map(int, input().split()))
ans = 0
dp = [0]*len(nums)
dp[-1] = 1
ans = 1
for i in range(len(nums)-2,-1,-1):
    max_val = 1
    num = nums[i]
    for j in range(i+1,len(nums)):
        if num < nums[j]:
            max_val = max(max_val,dp[j]+1)
    dp[i] = max_val
    ans = max(ans,max_val)

print(ans)