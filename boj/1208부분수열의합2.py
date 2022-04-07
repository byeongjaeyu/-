n,s = map(int, input().split())
nums = list(map(int, input().split()))
from itertools import combinations

ans = 0
for cnt in range(1,n+1):
    parts = combinations(nums,cnt)
    for part in parts:
        if sum(part) == s:
            ans += 1
print(ans)