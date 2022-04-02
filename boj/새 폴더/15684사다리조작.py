def go():
    start = [_ for _ in range(n)]
    for idx1 in range(h):
        for idx2 in range(n-1):
            if ladder_lst[idx1][idx2] == 1:
                start[idx2],start[idx2+1] = start[idx2+1],start[idx2]
    
    for s in range(len(start)):
        if start[s] != s:
            return False
    
    else:
        return True

def isrange(idx1:int,idx2:int):
    if(ladder_lst[idx1][idx2] == 1):
        return False
    
    if ((idx2+1<n-1) and ladder_lst[idx1][idx2+1]==0) or ((idx2+1>=n-1)):
        if ((idx2-1>=0) and ladder_lst[idx1][idx2-1]==0) or ((idx2-1<0)):
            return True

    return False

def dfs(idx1:int,idx2:int,cnt:int):
    global ans
    
    if cnt > 3:
        return
    
    if go() == True:
        if cnt < ans:
            ans = cnt
        return
    
    for idx11 in range(idx1,h):
        for idx22 in range(n-1):
            if isrange(idx11,idx22) == True:
                ladder_lst[idx11][idx22] = 1
                dfs(idx11,idx22,cnt+1)
                ladder_lst[idx11][idx22] = 0


n, m, h = map(int, input().split())
input_lst = [list(map(int, input().split())) for _ in range(m)]

ladder_lst = [[0] * (n-1) for _ in range(h)]

ans = 4

for input in input_lst:
    ladder_lst[input[0]-1][input[1]-1] = 1

dfs(0,0,0)

print(ans) if ans != 4 else print(-1)
