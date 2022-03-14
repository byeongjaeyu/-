a = int(input())
m = int(input())
wrong_button = list(map(int, input().split()))
dp = [0]*500001
dp[100] = 0

for i in range(99,-1):
    num = str(i)
    flag = True
    for n in num:
        if int(n) in wrong_button:
            flag = False
            break
    if flag:
        dp[i] = min(dp[i+1]+1,len(num))
    else:
        dp[i] = dp[i+1]+1

        
for i in range(101,500001):
    num = str(i)
    flag = True
    for n in num:
        if int(n) in wrong_button:
            flag = False
            break
    if flag:
        dp[i] = min(dp[i-1]+1,len(num))
    else:
        dp[i] = dp[i-1]+1



print(dp[a])