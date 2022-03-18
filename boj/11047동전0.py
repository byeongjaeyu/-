n,k = map(int, input().split())
coin_lst = [0]*10
for i in range(n):
    coin_lst[i] = int(input())

ans = 0

for i in range(n-1,-1,-1):
    val = coin_lst[i]
    while k>=val:
        k -= val
        ans += 1

print(ans)