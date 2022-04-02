n,m = map(int, input().split())
memo = dict()
for i in range(n):
    a,b = map(str,input().split())
    memo[a] = b
for i in range(m):
    a = input()
    print(memo[a])