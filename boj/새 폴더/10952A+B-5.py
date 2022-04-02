flag = True
while flag:
    n, m =map(int, input().split())
    if (n==0 and m == 0):
        flag = False
        continue
    print(n+m)