n = int(input())
nums = list(map(int, input().split()))
ans = [0]
for num in nums:
    if ans[-1]<num:
        ans.append(num)
    else:
        s=0
        e=len(ans)
        while s<e:
            m = (s+e)//2
            if ans[m]<num:
                s = m+1
            else:
                e = m
        ans[e] = num
print(len(ans)-1)