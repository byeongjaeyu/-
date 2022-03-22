from sys import stdin
input = stdin.readline
while True:
    num_lst = list(map(int ,input().split()))
    if len(num_lst) == 1:
        break
    else:
        k = num_lst[0]
        for i1 in range(1,k+1):
            for i2 in range(i1+1,k+1):
                for i3 in range(i2+1,k+1):
                    for i4 in range(i3+1,k+1):
                        for i5 in range(i4+1,k+1):
                            for i6 in range(i5+1,k+1):
                                print(num_lst[i1],num_lst[i2],num_lst[i3],num_lst[i4],num_lst[i5],num_lst[i6])
    
    print()

