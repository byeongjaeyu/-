from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
parent = [i for i in range(n)]
def findparent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findparent(parent[x])
        return parent[x]
def union(x,y):
    rootx = findparent(x)
    rooty = findparent(y)

    if rootx<rooty:
        parent[rooty] = rootx
    else:
        parent[rootx] = rooty

for i in range(1,m+1):
    s,e = map(int, input().split())
    if findparent(s) != findparent(e):
        union(s,e)
    else:
        print(i)
        break
else:
    print(0)