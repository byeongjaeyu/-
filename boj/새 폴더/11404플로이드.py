from sys import stdin
input = stdin.readline
n = int(input())
default = [[0xffffffff]*(n+1) for _ in range(n+1)]
m = int(input())
for i in range(m):
    u,v,w = map(int, input().split())
    default[u][v] = min(default[u][v],w)

for i in range(1,n+1):
    default[i][i] = 0

for node in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if(default[s][node]+default[node][e]<default[s][e]):
                default[s][e] = default[s][node]+default[node][e]

for i in range(1,n+1):
    for j in range(1,n+1):
        if default[i][j] == 0xffffffff:
            default[i][j] = 0

for i in range(1,n+1):
    print(*default[i][1:])
