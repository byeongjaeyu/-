from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline
nums = []
ans = []
while True:
    try:
        num = int(input())
        nums.append(num)
        if type(num) != int:
            break
    except:
        break

def solution(s:int,e:int):
    if s==e:
        ans.append(nums[s])
        return
    root = nums[s]
    idx = 0
    for i in range(s+1,e+1):
        if nums[i]>root:
            idx = i
            break
    if idx:
        left_s = s+1
        left_e = idx-1
        right_s = idx
        right_e = e
        if left_s<=left_e:
            solution(left_s,left_e)
        if right_s<=right_e:
            solution(right_s,right_e)
    else:
        solution(s+1,e)
    ans.append(root)

solution(0,len(nums)-1)

for i in range(len(ans)):
    print(ans[i])
