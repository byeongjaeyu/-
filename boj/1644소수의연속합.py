import math
n = int(input())
nums = [True]*(n+1)

for i in range(2,int(math.sqrt(n))+1):
    if nums[i] == True:
        j = 2
        while i*j<=n:
            nums[i*j] = False
            j += 1


ans = 0
pointer1 = 2
pointer2 = 2
s = 2
while True:
    if pointer1>n or pointer2>n: break
    if (s<n):
        i = 1
        while pointer2+i<n+1 and not nums[pointer2+i]:
            i += 1
        pointer2 += i
        s += pointer2
    if (s>=n):
        if s==n:ans += 1
        i = 1
        while pointer1+i<n+1 and not nums[pointer1+i]:
            i += 1
        s -= pointer1
        pointer1 += i

print(ans)

    
    
