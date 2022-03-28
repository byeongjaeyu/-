from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**5)
input = stdin.readline
v = int(input())
tree_lst = [[] for _ in range(v+1)]

for _ in range(v):
    lst = list(map(int, input().split()))
    for i in range(1,len(lst)-2,2):
        tree_lst[lst[0]].append([lst[i],lst[i+1]])

def dfs(n,d):
    global max_dis

    if max_dis[1] < d:
        max_dis = [n,d]
        
    for i in range(len(tree_lst[n])):
        node = tree_lst[n][i]
        if visited[node[0]] == 0:
            visited[node[0]] = 1
            dfs(node[0],d+node[1])
            visited[node[0]] = 0


visited = [0]*(v+1)
max_dis = [0,0]

visited[1] = 1
dfs(1,0)
visited[1] = 0

s = max_dis[0]
max_dis = [0,0]
visited[s] = 1

dfs(s,0)
print(max_dis[1])

