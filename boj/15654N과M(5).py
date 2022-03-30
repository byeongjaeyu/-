n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [0]*len(nums)
ans = []
def solution(i:int,j:int,lst:list):
    if j == m:
        temp = " ".join(map(str,lst))
        if temp not in ans:
            ans.append(temp)
    else:
        for k in range(len(nums)):
            if not visited[k]:
                visited[k] = 1
                solution(nums[k],j+1,lst+[nums[k]])
                visited[k] = 0

for i in range(len(nums)):
    visited[i] = 1
    solution(nums[i],1,[nums[i]])
    visited[i] = 0

for s in ans:
    print(s)