a = int(input())
m = int(input())
if m:
    wrong_button = set(list(map(int, input().split())))
else:
    wrong_button = set()

dp = [0xffffff]*500001
dp[100] = 0

channel = 500000

while True:
    if channel-500000 >= 499900:
        break

    for ch in str(channel):
        if int(ch) in wrong_button:
            channel += 1
            break
    else:
        break

dp[500000] = channel - 500000 + len(str(channel))

for i in range(99,-1,-1):
    num = str(i)
    flag = True
    for n in num:
        if int(n) in wrong_button:
            flag = False
            break
    if flag:
        dp[i] = min(dp[i+1]+1,len(num),dp[i])
    else:
        dp[i] = min(dp[i+1]+1,dp[i])

        
for i in range(101,500001):
    num = str(i)
    flag = True
    for n in num:
        if int(n) in wrong_button:
            flag = False
            break
    if flag:
        dp[i] = min(dp[i-1]+1,len(num),dp[i])
    else:
        dp[i] = min(dp[i-1]+1,dp[i])

for i in range(499999,99,-1):
    dp[i] = min(dp[i+1]+1,dp[i])

for i in range(1,101):
    dp[i] = min(dp[i-1]+1,dp[i])



print(dp[a])