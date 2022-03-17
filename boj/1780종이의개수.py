def solution(x:int,y:int,s:int):
    global plus1, minus1, zero
    if s == 1:
        return map_lst[x][y]
    else:
        div = s//3
        val1 = solution(x,y,div)
        val2 = solution(x,y+div,div)
        val3 = solution(x,y+(2*div),div)
        val4 = solution(x+div,y,div)
        val5 = solution(x+div,y+div,div)
        val6 = solution(x+div,y+(2*div),div)
        val7 = solution(x+(2*div),y,div)
        val8 = solution(x+(2*div),y+div,div)
        val9 = solution(x+(2*div),y+(2*div),div)

        lst = [val1,val2,val3,val4,val5,val6,val7,val8,val9]

        if val1 != None and val1==val2==val3==val4==val5==val6==val7==val8==val9:
            if val1 == 0:
                return 0
            elif val1 == -1:
                return -1
            elif val1 == 1:
                return 1
        else:
            for el in lst:
                if el == None:
                    continue
                elif el == -1:
                    minus1 += 1
                elif el == 1:
                    plus1 += 1
                elif el == 0:
                    zero += 1


n = int(input())
map_lst = [list(map(int, input().split())) for _ in range(n)]

minus1 = 0
zero = 0
plus1 = 0

val = solution(0,0,n)
if val == 0:
    zero += 1
elif val == -1:
    minus1 += 1
elif val == 1:
    plus1 += 1

print(minus1)
print(zero)
print(plus1)