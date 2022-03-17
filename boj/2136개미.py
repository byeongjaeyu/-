from sys import stdin
input = stdin.readline
n,l = map(int, input().split())

ant_lst = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    ant_lst[i] = [a,i]

max_dis = [0,0]
for i in range(n):
    if ant_lst[i][0] > 0:
        if max_dis[0] < l-ant_lst[i][0]:
            max_dis = [l-ant_lst[i][0],ant_lst[i][1]]
    else:
        if max_dis[0] < abs(ant_lst[i][0]):
            max_dis = [abs(ant_lst[i][0]),ant_lst[i][1]]

change = max_dis[1]
lst = []
cnt = 0
if ant_lst[max_dis[1]][0] > 0:
    for i in range(n):
        if abs(ant_lst[i][0]) > ant_lst[max_dis[1]][0]:
            lst.append(ant_lst[i][1])
            if ant_lst[i][0] < 0:
                cnt += 1
    lst.sort(key=lambda x:ant_lst[x][0])
    if cnt:
        change = lst[cnt-1]

else:
    for i in range(n):
        if abs(ant_lst[i][0]) < ant_lst[max_dis[1]][0]:
            lst.append(ant_lst[i][1])
            if ant_lst[i][0] > 0:
                cnt += 1
    lst.sort(key=lambda x:ant_lst[x][0], reverse=True)
    if cnt:
        change = lst[cnt-1]
            

print(change+1, max_dis[0])

