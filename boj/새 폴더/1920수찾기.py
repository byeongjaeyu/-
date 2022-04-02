n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

n_lst.sort()

for i in range(m):
    num = m_lst[i]
    s = 0
    e = n-1
    while s<=e:
        m = (s+e)//2
        if n_lst[m] == num:
            print(1)
            break
        if n_lst[m] > num:
            e = m-1
        else:
            s = m+1
    else:
        print(0)



