def solution(x,y,n):
    global n0,n1

    if n==1:
        return map_lst[x][y]

    val1 = 1
    val2 = 0

    d1 = solution(x,y,n//2)
    d2 = solution(x,y+(n//2),n//2)
    d3 = solution(x+(n//2),y,n//2)
    d4 = solution(x+(n//2),y+(n//2),n//2)

    lst = [d1,d2,d3,d4]

    for d in lst:
        if type(d) == int:
            val1 *= d
            val2 += d

    if (val1 == 1 or val2 == 0) and not(None in lst):
        if val1 == 1:
            return 1
        else:
            return 0
    else:
        for d in lst:
            if type(d) == int:
                if d == 1:
                    n1 += 1
                else:
                    n0 += 1

import sys
n = int(sys.stdin.readline())
map_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n0 = 0
n1 = 0
val = solution(0,0,n)
if val == 0:
    n0 += 1
elif val == 1:
    n1 += 1
print(n0)
print(n1)