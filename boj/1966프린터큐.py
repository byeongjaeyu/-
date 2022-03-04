for test in range(int(input())):
    n,m = map(int, input().split())
    important_lst = list(map(int ,input().split()))
    cnt = 1
    while True:
        if 0 == m:
            for j in range(1,len(important_lst)):
                if important_lst[j] > important_lst[0]:
                    p = important_lst.pop(0)
                    important_lst.append(p)
                    m = len(important_lst)-1

                    break
            else:
                print(cnt)
                break
        else:
            for j in range(0+1,len(important_lst)):
                if important_lst[j] > important_lst[0]:
                    p = important_lst.pop(0)
                    important_lst.append(p)
                    m -= 1

                    break
            else:
                p = important_lst.pop(0)
                m -= 1
                cnt += 1

            