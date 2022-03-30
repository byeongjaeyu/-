n = int(input())
dp = [[[0] * (1<<10) for _ in range(10)] for __ in range(101)]

def stair(n1:int,n2:int,n3:int): #n1:현재숫자몇개썻나, n2:앞에시작하는숫자, n3:현재비트마스킹
    if dp[n1][n2][n3]:
        return dp[n1][n2][n3]

    if n1 == n:
        if n3 == (1<<10) - 1:
            return 1
        else:
            return 0
    
    else:
        if n2+1<=9:
            dp[n1][n2][n3] += stair(n1+1,n2+1,n3|1<<(n2+1))
        if n2-1>=0:
            dp[n1][n2][n3] += stair(n1+1,n2-1,n3|1<<(n2-1))

    return dp[n1][n2][n3]


ans = 0
for i in range(1,10):
    ans += stair(1,i,1<<i)

print(ans%1000000000)
