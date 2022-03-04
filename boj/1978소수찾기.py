n = int(input())
num_lst = list(map(int, input().split()))
ans = 0
for i in range(n):
    num = num_lst[i]
    for div in range(2,int(num**0.5)+1):
        if num%div == 0:
            break
    else:
        ans += 1

print(ans)