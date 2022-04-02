n = int(input())

def contain5(n:int):
    d = 2
    contain5cnt = 0
    while d<=n:
        if not n % d:
            n /= d
            if d == 5:
                contain5cnt += 1
        else:
            d += 1

    return contain5cnt

ans = 0
for i in range(1,n+1):
    ans += contain5(i)

print(ans)