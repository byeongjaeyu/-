n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
def solution(cnt:int,idx:int):
    if cnt == m:
        print(' '.join(map(str,ans)))
        return
    else:
        for i in range(idx,n):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            ans.append(nums[i])
            solution(cnt+1,i)
            ans.pop(-1)

for i in range(n):
    if i>=1 and nums[i] == nums[i-1]:
        continue
    ans.append(nums[i])
    solution(1,i)
    ans.clear()