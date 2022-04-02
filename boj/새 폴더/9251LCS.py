a = input()
b = input()

dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i1 in range(len(a)+1):
    for i2 in range(len(b)+1):
        if i1==0 or i2==0:
            dp[i1][i2] = 0
        else:
            if a[i1-1] == b[i2-1]:
                dp[i1][i2] = 
