def solution(h:int):
    global ans
    t = 0
    can = b
    ing = 0
    for i in range(n):
        for j in range(m):
            if map_lst[i][j] > h:
                needs = map_lst[i][j] - h
                t += 2*needs
                ing += needs
            elif map_lst[i][j] < h:
                needs = h - map_lst[i][j]
                t += needs
                ing -= needs
            if t > ans[0]:
                return
    if can + ing >= 0:
        if t < ans[0]:
            ans = [t,h]
        elif t == ans[0]:
            if h > ans[1]:
                ans[1] = h
            
n,m,b = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(n)]
max_map = 0
ans = [0xffffffff,0]
for i in range(n):
    for j in range(m):
        max_map = max(max_map,map_lst[i][j])

if max_map == 0:
    print('0 0')
else:
    for h in range(0,max_map+1):
        solution(h)
    print(*ans)
    