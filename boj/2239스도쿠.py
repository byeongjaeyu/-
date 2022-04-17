board = [list(map(int, input())) for _ in range(9)]

cnt = 0
zero_idx = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_idx.append([i,j])
            cnt += 1

def fill(c:int):
    if c == len(zero_idx):
        for i in range(9):
            print(''.join(map(str,board[i])))
        return 1
    i = zero_idx[c][0]; j = zero_idx[c][1]
    for num in range(1,10):
        if num not in board[i]:
            flag = True
            for k in range(9):
                if board[k][j] == num:
                    flag = False
                    break

            if not flag:
                continue

            flag = True
            for ii in range(i//3*3,i//3+3):
                for jj in range(j//3*3,j//3+3):
                    if board[ii][jj] == num:
                        flag = False
                        break
                if not flag:
                    break

            if not flag:
                continue

            board[i][j] = num
            if fill(c+1):
                return 1
            board[i][j] = 0

fill(0)