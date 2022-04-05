n = int(input())
n = n//3
cnt = 0
while n!=1:
    n //= 2
    cnt += 1
default_height = 6
default_width = 11
if cnt:
    for i in range(cnt-1):
        default_height = default_height * 2
        default_width = (default_width * 2) + 1
board = [[" "]*default_width for _ in range(default_height)]
def getlevel(sx,ex):
    cnt = 0
    temp = ex-sx
    while temp != 10:
        temp -= 1
        temp //= 2
        cnt += 1
    return cnt

def writestar(sx,ex,ey):
    level = getlevel(sx,ex)
    if ex-sx != 10:
        temp = 5
        if level:
            for i in range(level-1):
                temp *= 2
                temp += 1
        mid = (sx+ex)//2
        writestar(sx,mid-1,ey)
        writestar(mid+1,ex,ey)
        writestar(mid-temp,mid+temp,ey-(6*(2**(level-1))))
    else:
        global board
        board[ey][sx:ex+1] = ['*','*','*','*','*',' ','*','*','*','*','*']
        board[ey-1][sx+1:ex] = ['*',' ','*',' ',' ',' ','*',' ','*']
        board[ey-2][sx+2:ex-1] = ['*',' ',' ',' ',' ',' ','*']
        board[ey-3][sx+3:ex-2] = ['*','*','*','*','*']
        board[ey-4][sx+4:ex-3] = ['*',' ','*']
        board[ey-5][sx+5:ex-4] = ['*']

if cnt:
    writestar(0,default_width-1,default_height-1)
    for i in range(default_height):
    # print(len(''.join(map(str,board[i]))))
        print(''.join(map(str,board[i])))
else:
    print('  *  ')
    print(' * *  ')
    print('*****')

