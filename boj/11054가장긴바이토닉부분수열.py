n = int(input())
nums = list(map(int, input().split()))
dp_up = [1]*(n+1)
dp_down = [1]*(n+1)
for i in range(1,len(nums)):
    max_val = 1
    num = nums[i]
    for j in range(0,i):
        if nums[j] < num:
            max_val = max(max_val,dp_up[j]+1)
    dp_up[i] = max_val

for i in range(len(nums)-2,-1,-1):
    max_val = 1
    num = nums[i]
    for j in range(i+1,len(nums)):
        if nums[j] < num:
            max_val = max(max_val,dp_down[j]+1)
    dp_down[i] = max_val

ans = 0
for i in range(0,len(nums)):
    ans = max(ans,dp_up[i]+dp_down[i]-1)

print(ans)

