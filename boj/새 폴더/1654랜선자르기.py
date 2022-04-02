k,n = map(int,input().split())
line_lst = [int(input()) for _ in range(k)]

s = 0
e = max(line_lst)+1
flag = True
while (s<e):
    mid = (s+e)//2
    cnt = 0
    for line in line_lst:
        cnt += line//mid
    
    if cnt >= n:
        s = mid+1
    else:
        e = mid

print(s-1)