n = int(input())
cur_sum = 0
cnt = 0
for i in range(int(n**0.5)+1,0,-1):
    if cur_sum == n:
        break
    while True:
        if cur_sum + i**2 > n:
            break
        else:
            cur_sum += i**2
            cnt += 1

print(cnt)