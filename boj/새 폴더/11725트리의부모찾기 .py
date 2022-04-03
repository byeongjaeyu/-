from sys import setrecursionlimit
setrecursionlimit(10**5)
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

p = [0]*(n+1)
visited = [0]*(n+1)
def getparent(node:int):
    for child in tree[node]:
        if not visited[child]:
            p[child] = node
            visited[child] = 1
            getparent(child)

visited[1] = 1
getparent(1)
for i in range(2,n+1):
    print(p[i])