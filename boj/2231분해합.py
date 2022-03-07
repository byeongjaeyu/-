n = int(input())
n1 = 1

while n1<=n:
    save = n1
    res = save
    while save!=0:
        res += save%10
        save //= 10
    if res == n:
        print(n1)
        break
    n1 += 1
else:
    print(0)
