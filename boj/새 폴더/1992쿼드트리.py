

def solution(x:int,y:int,s:int):
    global ans
    if s == 1:
        return map_lst[x][y]

    val1 = solution(x,y,s//2)
    val2 = solution(x,y+(s//2),s//2)
    val3 = solution(x+(s//2),y,s//2)
    val4 = solution(x+(s//2),y+(s//2),s//2)

    if val1 == val2 == val3 == val4:
        if val1 == '1':
            return '1'
        elif val1=='0':
            return '0'
    return '({}{}{}{})'.format(val1,val2,val3,val4)
        



n = int(input())
map_lst = [list(map(str,input())) for _ in range(n)]



ans = solution(0,0,n)

print(ans)