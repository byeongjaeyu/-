input_lst = list(map(int, input().split()))
if input_lst[0] == 1:
    for i in range(1,len(input_lst)):
        if input_lst[i] != input_lst[0] + i:
            print('mixed')
            break
    else:
        print('ascending')

elif input_lst[0] == 8:
    for i in range(1,len(input_lst)):
        if input_lst[i] != input_lst[0] - i:
            print('mixed')
            break
    else:
        print('descending')

else:
    print('mixed')
