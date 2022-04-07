from sys import stdin,stdout,setrecursionlimit
input = stdin.readline
print = stdout.write
def solution(node:int):

        if dp[node] != -1:
            return dp[node]

        elif len(orders[node]) == 0:
            dp[node] = delays[node-1]
            return dp[node]

        else:
            max_val = 0
            for order in orders[node]:
                if dp[order] != -1:
                    max_val = max(max_val,dp[order])
                else:
                    max_val = max(max_val,solution(order))
            dp[node] = max_val + delays[node-1]
            return dp[node]

setrecursionlimit(1001)
for test in range(int(input())):
    n,k = map(int, input().split())
    delays = list(map(int, input().split()))
    orders = [[] for _ in range(n+1)]
    for i in range(k):
        a,b = map(int, input().split())
        orders[b] += [a]
    des = int(input())
    dp = [-1]*(n+1)
    
    solution(des)

    print(str(dp[des])+'\n')
