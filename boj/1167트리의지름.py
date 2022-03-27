from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**5)
input = stdin.readline
v = int(input())
tree_lst = [0]+[list(map(int, input().split())) for _ in range(v)]

def dfs(n,d):
    global max_dis
    if max_dis[1] < d:
        max_dis = [n,d]
    for i in range(1,len(tree_lst[n])-1,2):
        node = tree_lst[n][i]
        if visited[node] == 0:
            visited[node] = 1
            dfs(node,d+tree_lst[n][i+1])
            visited[node] = 0

visited = [0]*(v+1)
max_dis = [0,0]
visited[1] = 1
dfs(1,0)
s = max_dis[0]
visited = [0]*(v+1)
max_dis = [0,0]
visited[s] = 1
dfs(s,0)
print(max_dis[1])

