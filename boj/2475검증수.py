a = list(map(int,input().split()))
ans = 0
for i in range(len(a)):
    ans += a[i]**2
print(ans%10)
