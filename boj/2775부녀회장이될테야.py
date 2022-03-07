n = int(input())
ppls = [[0]*14 for _ in range(14)]
for i in range(14):
    ppls[0][i] = i+1
for i1 in range(1,14):
    for i2 in range(14):
        for i3 in range(0,i2+1):
            ppls[i1][i2] += ppls[i1-1][i3]
for i in range(n):
    k = int(input())
    n = int(input())
    print(ppls[k][n-1])
