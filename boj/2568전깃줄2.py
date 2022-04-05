from sys import stdin
input = stdin.readline
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x:x[0])
dp = [[0,0] for _ in range(lines[-1][0]+1)]

max_vall = 0
max_origin = 0

for i in range(len(lines)):
    dp[lines[i][0]] = [1,lines[i][0]]
    max_val = 1
    origin = 0
    if i>=1:
        for j in range(i):
            if lines[j][1]<lines[i][1]:
                if max_val < dp[lines[j][0]][0]+1:
                    max_val = dp[lines[j][0]][0]+1
                    origin = dp[lines[j][0]][1]
    
    if max_val != 1:
        dp[lines[i][0]] = [max_val,origin]
        if max_val > max_vall:
            max_vall = max_val
            max_origin = origin


ans = []
cnt = 0
for i in range(len(dp)):
    if dp[i][0] != 0:
        if dp[i][1] != origin:
            cnt += 1
            ans.append(i)

print(cnt)
for i in range(len(ans)):
    print(ans[i])
    
