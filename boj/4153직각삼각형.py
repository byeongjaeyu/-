while True:
    a,b,c = map(int, input().split())
    if(a==0 and b==0 and c==0):
        break
    else:
        num_lst = [a,b,c]
        num_lst.sort()
        if num_lst[0]**2 + num_lst[1]**2 == num_lst[2]**2:
            print('right')
        else:
            print('wrong')