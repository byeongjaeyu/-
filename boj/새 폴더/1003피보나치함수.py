dp = [[0,0] for _ in range(41)] #0, 1
dp[0] = [1,0]
dp[1] = [0,1]

def fibo(n):
    if dp[n] != [0,0]:
        return dp[n]
    else:
        n1 = fibo(n-1)
        n2 = fibo(n-2)
        dp[n] = [n1[0]+n2[0],n1[1]+n2[1]]
        return dp[n]

for n in range(0,41):
    if dp[n] == [0,0]:
        fibo(n)

for test in range(int(input())):
    n = int(input())
    print(dp[n][0],dp[n][1])